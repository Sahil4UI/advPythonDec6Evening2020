import pygame
pygame.init()

width = 1000
height = 500
screen = pygame.display.set_mode((width, height))

white = 255,255,255
x = 0
y = 0
moveX = 1
moveY = 1
while True:
    for event in pygame.event.get():
        # print(event)
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    screen.fill(white)
    # surafce, color, [x,y,w,h]
    pygame.draw.circle(screen,(255,0,0),[x,y], 50)

    x += moveX
    y += moveY

    if x > width - 50:
        moveX = -1
    elif x < 50:
        moveX = 1
    elif y > height - 50:
        moveY = -1
    elif y < 50:
        moveY = 1

    pygame.display.update()
