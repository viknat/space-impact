import sys, pygame
from pygame.locals import *
pygame.init()

width, height = 640, 480
posx,posy = 0,0
black = 0,0,0

ship = pygame.image.load("shuttle.gif")
shiprect = ship.get_rect()

bullet = pygame.image.load("bullet_friendly.gif")
bullrect = ship.get_rect()

background = pygame.image.load("space.gif")
screen = pygame.display.set_mode((width, height))
screen.blit (background, (0,0))

done = False

screen.blit (ship, (posx, posy))
pygame.display.flip()

bullets = list()

pygame.key.set_repeat(10,10)
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            pygame.quit()
            sys.exit()

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT:
                posx += 10
        

            if event.key == pygame.K_LEFT:
                posx -= 10
                
            if event.key == pygame.K_UP:
                posy -= 10
                
            if event.key == pygame.K_DOWN:
                posy += 10
                       
            if event.key == pygame.K_SPACE:
                bullets.append([posx, posy])

    
    screen.blit (background, (0,0))
    screen.blit (ship, (posx, posy))
    for bullpos in bullets:
        bullpos[0],bullpos[1] = bullpos[0], bullpos[1] - 1
        screen.blit (bullet, (bullpos[0], bullpos[1]))
    pygame.display.flip()
