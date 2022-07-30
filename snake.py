import pygame
pygame.init()
dis=pygame.display.set_mode((1200,800))


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

while not game_over:
    for event in pygame.event.get():
        if event.type==pygame.QUIT:
            game_over=True
        # hier wird ein Pfeil gedrückt
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                x1_change = -10
                y1_change = 0
            elif event.key == pygame.K_RIGHT:
                x1_change = 10
                y1_change = 0
            elif event.key == pygame.K_UP:
                y1_change = -10
                x1_change = 0
            elif event.key == pygame.K_DOWN:
                y1_change = 10
                x1_change = 0
        # pygame.draw.rect(dis,blue,[200,150,10,10])

        pygame.draw.circle(dis,blue,(x1,y1),10)
       
        # update display

        # check if boundary hit
        
        x1 += x1_change
        y1 += y1_change

        if 0<=x1<=1200 and 0<=y1<=800:
        #dis.fill(white)
            pygame.draw.circle(dis,red,(x1,y1),10)
            pygame.display.update()
        else:
            x1 -= x1_change
            y1 -= y1_change


        clock.tick(30)
 
pygame.quit()
quit()