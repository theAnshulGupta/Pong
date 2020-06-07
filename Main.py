import pygame
import random 
import time

pygame.init()

gameDisplay=pygame.display.set_mode((600,630)) 

pygame.display.set_caption("Pong")

white=(255,255,255)#r,g,b
black=(0,0,0)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
aquamarine2=(118,238,198)

gameDisplay.fill(black)


rectx1=10
recty1=200

rectx2=570
recty2=200

redup=False
reddown=False

gup=False
gdown=False

ballx1=300
bally1=300

velx1=1
vely1=1

reds=0
greens=0
spacebutton=False

gameStart=False
def text(msg,x,y,color=white, size=10):
    font=pygame.font.SysFont('Comic Sans MS', size)
    m=font.render(msg, True, color)
    gameDisplay.blit(m,(x,y))
    

def textAriel(msg,x,y,color=white, size=10):
    font=pygame.font.SysFont('Ariel', size)
    m=font.render(msg, True, color)
    gameDisplay.blit(m,(x,y))
    

#all below required
clock=pygame.time.Clock()


while True:

    pygame.display.update()
    gameDisplay.fill(black)

    for event in pygame.event.get():

        if event.type==pygame.QUIT: 
            pygame.quit()
            quit()

        if event.type==pygame.KEYDOWN:
            if event.key==pygame.K_w:
                redup=True
            elif event.key==pygame.K_a:
                reddown=True
            elif event.key==pygame.K_UP:
                gup=True
            elif event.key==pygame.K_DOWN:
                gdown=True
            elif event.key==pygame.K_SPACE:
                spacebutton=True

        if event.type==pygame.KEYUP:
            if event.key==pygame.K_w:
                redup=False
            elif event.key==pygame.K_a:
                reddown=False
            elif event.key==pygame.K_UP:
                gup=False
            elif event.key==pygame.K_DOWN:
                gdown=False
            elif event.key==pygame.K_SPACE:
                spacebutton=False
        

    clock.tick(200)
#boundries

    if gameStart==False:
        textAriel('Press Space to Begin', 135,300, white, 50)
        textAriel('Anshul Games Inc 2017', 230,615,white,20)
        if spacebutton==True:
            gameStart=True
    elif gameStart==True:
        
        if redup==True and recty1!=0:
            recty1-=1
        if reddown==True and recty1!=400:
            recty1+=1


        if gup==True and recty2!=0:
            recty2-=1
        if gdown==True and recty2!=400:
            recty2+=1

        ballx1+=velx1
        bally1+=vely1
        if (ballx1+20==rectx2 and bally1>=recty2 and bally1<=recty2+200) or (ballx1-20==rectx1+20 and bally1>=recty1 and bally1<=recty1+200):
            velx1=-1*velx1
        if bally1==580 or bally1==20:
            vely1=-1*vely1
        if ballx1==620:
            reds+=1
            print(greens)
            print(reds)
            ballx1=bally1=300
            rectx1=10
            recty1=200
            rectx2=570
            recty2=200
            velx1=1
            vely1=1
        
        elif ballx1==-20:
            greens+=1
            print(greens)
            print(reds)
            ballx1=bally1=300
            rectx1=10
            recty1=200
            rectx2=570
            recty2=200
            velx1=-1
            vely1=1
         
        pygame.draw.rect(gameDisplay, white, (0,600,600,30))    
        text('PONG', 280,605, blue, 15)
        textAriel(str(reds), 10,610, red, 20)
        textAriel(str(greens), 580,610, green, 20)
        pygame.draw.line(gameDisplay, white, (300,0), (300,600))
        pygame.draw.circle(gameDisplay, white, (300,300),60, 1)
        pygame.draw.circle(gameDisplay, blue, (ballx1,bally1), 20)
        pygame.draw.rect(gameDisplay, red, (rectx1,recty1,20,200))
        pygame.draw.rect(gameDisplay, green, (rectx2,recty2,20,200))
