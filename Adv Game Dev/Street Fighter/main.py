import pygame
import random


width = 1200
height = 600

screen = pygame.display.set_mode((width,height))

black = 0,0,0
white = 255,255,255
red = 255,0,0


class SpriteSheet():
    def __init__(self,file_name):
        pygame.sprite.Sprite.__init__(self)
        self.spriteSheet= file_name
    
    def getImage(self,x,y,width,height):
        image = pygame.Surface((width,height))
        image.blit(self.spriteSheet,(0,0),(x,y,width,height))
        image.set_colorkey(black)
        
        return image
        

class Player(pygame.sprite.Sprite):
    standingFrames = []
    kickFrames = []
    
    def __init__(self):
        super().__init__()
        spriteSheet = SpriteSheet(ken)
        self.image = spriteSheet.getImage(6,11,42,90)
        self.standingFrames.append(self.image)
        
        self.image = spriteSheet.getImage(248,11,48,88)
        self.standingFrames.append(self.image)
                                
        self.image = spriteSheet.getImage(302,13,46,88)
        self.standingFrames.append(self.image)
        
        
        
        self.image = spriteSheet.getImage(0,254,58,96)
        self.kickFrames.append(self.image)
        
        self.image = spriteSheet.getImage(53,252,82,96)
        self.kickFrames.append(self.image)
        
        self.rect = self.image.get_rect()
        self.rect.x=250
        self.rect.y=height-300
        self.pos=0
        
        self.stand=True
        self.kick = False
    
    def update(self):
        self.pos +=2
        keypressed = pygame.key.get_pressed()
        if keypressed[pygame.K_SPACE]:
            self.kick =True
            self.stand = False
        else:
            self.kick = False
            self.stand =True
            
            
        if self.stand:
            frame = self.pos // 30 % len(self.standingFrames)
            self.image= self.standingFrames[frame]
        
        elif self.kick:
            frame = self.pos // 30 % len(self.kickFrames)
            self.image= self.kickFrames[frame]
        
                                    
ken = pygame.image.load(r"Street Fighter\assets\ken.png")

all_Sprites = pygame.sprite.Group()
player_1 = Player()
all_Sprites.add(player_1)


FPS = 10
clock = pygame.time.Clock()
while True:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            pygame.quit()
            quit()

            
    screen.fill(white)
    all_Sprites.draw(screen)
    all_Sprites.update()
    pygame.display.update()
    clock.tick(FPS)

    
    
    