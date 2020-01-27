import pygame,time,random

white=(255,255,255)
black=(0,0,0)
red=(255,0,0)
blue=(0,0,255)
green=(0,255,0)
window_height=600
screen_width=600
screen_height=500


pygame.init()
window=pygame.display.set_mode((400,window_height))
pygame.display.set_caption('Flappy Bird')
bird_x=int(screen_width/14)
bird_y=250
fps=30
c=0

bird_height=40
bird_width=40
bird_color=blue

clock=pygame.time.Clock()

font=pygame.font.Font(None,25)



def msgToScrn(msg,color,mx,my):
    screen_text=font.render(msg,True,color)
    window.blit(screen_text,[mx,my])



picture = pygame.image.load('flappy.png')
picture = pygame.transform.scale(picture, (bird_width,bird_height))

def gameLoop():

    c = 0
    bird_y = 250
    gameExit = False
    gameOver = False
    obstacle_x = [screen_width, screen_width + 2 * (int(screen_width / 7)), screen_width + 4 * (int(screen_width / 7)),
                  screen_width + 6 * (int(screen_width / 7))]
    obstacle_yup = 0
    obstacle_ydown = [random.randint(int(screen_height * 50 / 100), int(screen_height * 75 / 100)),
                      random.randint(int(screen_height * 50 / 100), int(screen_height * 75 / 100)),
                      random.randint(int(screen_height * 50 / 100), int(screen_height * 75 / 100)),
                      random.randint(int(screen_height * 50 / 100), int(screen_height * 75 / 100))]
    obstacle_heightup = [obstacle_ydown[0] - int(screen_height * 25 / 100),
                         obstacle_ydown[1] - int(screen_height * 25 / 100),
                         obstacle_ydown[2] - int(screen_height * 25 / 100),
                         obstacle_ydown[3] - int(screen_height * 25 / 100)]
    obstacle_width = 70
    obstacle_heightdown = [screen_height - obstacle_ydown[0], screen_height - obstacle_ydown[1],
                           screen_height - obstacle_ydown[2], screen_height - obstacle_ydown[3]]
    i = 0
    count = 0


    while not gameExit:

        for ob1count in range(4):
            obstacle_x[ob1count]=obstacle_x[ob1count]-5

        #if(obstacle_x[i] in range(int(screen_width/14+31),int(screen_width/14+40))):
        #    count=count+1
        if (obstacle_x[i] in range(int(screen_width / 14),int(screen_width / 13))):
            count = count + 1

        if(obstacle_x[i] in range(-int(screen_width/6.5),-int(screen_width/7))):
            obstacle_ydown[i] = random.randint(int(screen_height * 50 / 100), int(screen_height * 75 / 100))
            obstacle_heightup[i] = obstacle_ydown[i] - int(screen_height * 25 / 100)
            obstacle_x[i] = screen_width
            obstacle_heightdown[i] = screen_height - obstacle_ydown[i]

            i=i+1
            if(i==4):
                i=0

        while gameOver==True:
            if gameOver:
                time.sleep(1)
                window.fill(white)
                msgToScrn("GameOver ,Press  upper arrow key", red, int(screen_width /4),
                          int(screen_height / 2))
                pygame.display.update()

                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        gameExit = True
                        gameOver = False
                    elif event.type == pygame.KEYDOWN:
                        if event.key in [pygame.K_UP, pygame.K_CAPSLOCK]:

                            gameOver = False
                            gameLoop()

                        elif event.key in [pygame.K_q, pygame.K_CAPSLOCK]:

                            gameExit = True
                            gameOver = False

        c=c-1

        for event in pygame.event.get():
            c=c-1
            if event.type==pygame.QUIT:
                gameExit=True
            if event.type==(pygame.KEYDOWN):
                if event.key==pygame.K_UP:
                    bird_y=bird_y-8
                    c=9

        if(c<0):
            bird_y = bird_y + 8
        elif(c>3):
            bird_y = bird_y - 8
        window.fill(black)

        #pygame.draw.rect(window, bird_color, [bird_x, bird_y, bird_height,bird_width])
        window.blit(picture,(bird_x,bird_y))


        if(obstacle_x[i] in range(int(screen_width / 14)-68,int(screen_width / 14)+39) ):
            if(bird_y in range(0,obstacle_heightup[i]) ):
                gameOver=True
            if(bird_y in range(obstacle_ydown[i]-38,screen_height)):
                gameOver = True


        if(bird_y>475 or bird_y<-40):
            gameOver=True
        for obcounter in range(4):
            pygame.draw.rect(window, green, [obstacle_x[obcounter], obstacle_yup,obstacle_width, obstacle_heightup[obcounter] ])
            pygame.draw.rect(window, green, [obstacle_x[obcounter], obstacle_ydown[obcounter],obstacle_width, obstacle_heightdown[obcounter] ])
        msgToScrn("Score = " + str( count ), red,400, 510)

        pygame.display.update()
        clock.tick(fps)
    pygame.quit()
    quit()

gameLoop()