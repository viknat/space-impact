import sys, pygame
from pygame.locals import *
pygame.init()

width, height = 640, 480
speed = [0,0]
black = 0,0,0

ball = pygame.image.load("ball1.png")
ballrect = ball.get_rect()

background = pygame.image.load("Grass.png")
screen = pygame.display.set_mode((width, height))
screen.blit (background, (0,0))

done = False

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: done = True

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                speed = [1,0]
        

            if event.key == pygame.K_LEFT:
                speed = [-1,0] 
                
            if event.key == pygame.K_UP:
                speed = [0,-1] 
                
            if event.key == pygame.K_DOWN:
                speed = [0,1]
                
        else: speed = [0,0]       


    ballrect = ballrect.move(speed)
    if ballrect.left < 0 or ballrect.right > width:
        speed[0] = -speed[0]
    if ballrect.top < 0 or ballrect.bottom > height:
        speed[1] = -speed[1]

    screen = pygame.display.set_mode((width, height))
    screen.blit (background, (0,0))
    screen.blit (ball, ballrect)
    pygame.display.flip()

