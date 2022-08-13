import pygame
import cv2
from numpy import random

pygame.init()
display=pygame.display.set_mode((1200,800))

fly = pygame.image.load('C:\\Repos\\Snake-game\\pics\\40840-200.png')
fly = pygame.transform.scale(fly, (40, 40))

milliseconds_delay = 6000
enemy_spawn_event = pygame.USEREVENT + 1
pygame.time.set_timer(enemy_spawn_event, milliseconds_delay) # generates spawn event


pygame.display.set_caption('Schlangenspiel von Michael')

white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)
blue = (0, 0, 255)

#initializing values
game_over=False

y1 = 600
x1 = 400

x1_change = 0       
y1_change = 0

clock = pygame.time.Clock()

fly_x = random.randint(30,1100)
fly_y = random.randint(30,700)
grid_const = 15
while not game_over:
    for event in pygame.event.get():
        # event happens
        if event.type==pygame.QUIT:
            game_over=True
        # hier wird ein Pfeil gedrückt
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -grid_const
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = grid_const
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -grid_const
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = grid_const
                x1_change = 0
        if event.type == enemy_spawn_event:
            fly_x = random.randint(0,1200)
            fly_y = random.randint(0,800)

        # pygame.draw.rect(dis,blue,[200,150,10,10])
       
        # update display

        # check if boundary hit
        
        x1 += x1_change
        y1 += y1_change

        # check for catching the fly
        # if coordinates overlap, respawn fly
        if  (x1-grid_const < fly_x+20 < x1+grid_const) and (y1-grid_const < fly_y+20 < y1+grid_const):
            fly_x = random.randint(0,1200)
            fly_y = random.randint(0,800)
            pygame.time.set_timer(enemy_spawn_event, milliseconds_delay)



        if 0<=x1<=1200 and 0<=y1<=800:
            display.fill(white)
            pygame.draw.circle(display,red,(x1,y1),10)
            display.blit(fly,(fly_x,fly_y))
            
            pygame.display.update()
            print(x1,y1,fly_x,fly_y)
        else:
            x1 -= x1_change
            y1 -= y1_change


        clock.tick(30)
 
pygame.quit()
quit()