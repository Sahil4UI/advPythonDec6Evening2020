import pygame,random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width,height))

white = 255,255,255
black = 0,0,0
red = 255,0,0
blue = 0,0,255
green = 0,255,0

class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill(red)
        self.rect=self.image.get_rect()
        self.rect.x=width/2
        self.rect.y = height-50
        self.moveX=0
        self.health=100
    def update(self):
        keyPress = pygame.key.get_pressed()
        if keyPress[pygame.K_RIGHT]:
            self.moveX = 5
        elif keyPress[pygame.K_LEFT]:
            self.moveX = -5
        else:
            self.moveX =0
            
        self.rect.x += self.moveX
        self.hit = pygame.sprite.groupcollide(playerGroup,enemyGroup,False,True)
        if self.hit:
            self.health -=5
        self.playerHealth()
    def playerHealth(self):
        pygame.draw.rect(screen,green, [5,5,self.health ,25])
    
    def Shoot(self):
        bulletX  = self.rect.x + self.image.get_width()/2
        bulletY  = self.rect.y
        bullet = Bullet(bulletX,bulletY)
        bulletGroup.add(bullet)
        all_sprites.add(bullet)
    
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.Surface((50,50))
        self.image.fill(black)
        self.rect=self.image.get_rect()
        self.rect.x=random.randint(0,width -50)
        self.rect.y = random.randint(0,height-50)
        self.moveY = random.randint(1,4)
        
    def update(self,*args):
        self.rect.y += self.moveY
        if self.rect.y > height:
            self.rect.y = random.randint(-height,0)



class Bullet(pygame.sprite.Sprite):
    def __init__(self,x,y):
        super().__init__()
        self.image = pygame.Surface((6,14))
        self.image.fill(blue)
        self.rect = self.image.get_rect()
        self.rect.x = x
        self.rect.y = y
        self.moveY=-3
    
    def update(self):
        self.rect.y += self.moveY
        
        if self.rect.y<0:
            self.kill()
            
    
all_sprites = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
playerGroup = pygame.sprite.Group()
playerGroup.add(player)
bulletGroup = pygame.sprite.Group()
enemyGroup = pygame.sprite.Group()

for i in range(20):
    enemy = Enemy()
    enemyGroup.add(enemy)
    all_sprites.add(enemy)

FPS = 100
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                player.Shoot()
    
    hit = pygame.sprite.groupcollide(bulletGroup,enemyGroup,True,True)            
            
    screen.fill(white)
    all_sprites.draw(screen)
    all_sprites.update()
    pygame.display.update()
    clock.tick(FPS)

