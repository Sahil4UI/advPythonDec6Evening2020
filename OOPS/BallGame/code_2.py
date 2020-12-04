import pygame
import random
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

white = 255,255,255

class Ball:
    def __init__(self):
        self.x = 0
        self.y = 0
        self.moveX = random.randint(1,4)
        self.moveY = random.randint(1,4)

    def update(self):

        self.x += self.moveX
        self.y += self.moveY

        if self.x > width - 50:
            self.moveX = -random.randint(1,4)
        elif self.x < 50:
            self.moveX = random.randint(1,4)
        elif self.y > height - 50:
            self.moveY = -random.randint(1,4)
        elif self.y < 50:
            self.moveY = random.randint(1,4)

# ball_1 = Ball()
# ball_2 = Ball()

ballsList = []
for i in range(10):
    ball = Ball()
    ballsList.append(ball)

while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # surafce, color, [x,y,w,h]
    # pygame.draw.circle(screen,(255,0,0),[ball_1.x, ball_1.y], 50)
    # ball_1.update()
    #
    # pygame.draw.circle(screen, (255, 0, 0), [ball_2.x, ball_2.y], 50)
    # ball_2.update()

    for i in range(len(ballsList)):
        pygame.draw.circle(screen, (255, 0, 0), [ballsList[i].x, ballsList[i].y], 50)
        ballsList[i].update()

    pygame.display.update()
