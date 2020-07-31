import pygame,sys,math
#from pygame.locals import *

FPS = 70
WINDOWWIDTH = 640 # size of window's width in pixels
WINDOWHEIGHT = 480 # size of windows' height in pixels

ORGIN = (0,0)
SUN_POSITION = (20,20)
CLOUD_1_POSITION = (240,50)
CLOUD_2_POSITION = (490,30)
HOUSE_POSITION = (195,165)
FLOWER_POSITION = (172,405)

blackboard  = pygame.image.load('blackboardbackground.png')
chalksun = pygame.image.load('chalksun.png')
chalkcloud1 = pygame.image.load('chalkcloud1.png')
chalkcloud2 = pygame.image.load('chalkcloud2.png')
chalkhouse = pygame.image.load('chalkhouse.png')
flower = pygame.image.load('flower.png')
honeybee1 = pygame.image.load('honeybee1_small.png')
honeybee2 = pygame.image.load('honeybee2_small.png')


pygame.init()
butx = 100
buty = 380
a = 70
d = 0
hx = 165
hy = 320
  
FPSCLOCK = pygame.time.Clock()
drawboard = pygame.display.set_mode((WINDOWWIDTH, WINDOWHEIGHT))
pygame.display.set_caption('Honey bee')

honeyBeeSwitch = True
while True:

    

    drawboard.blit(blackboard,ORGIN)
    drawboard.blit(chalksun,SUN_POSITION)
    drawboard.blit(chalkcloud1,CLOUD_1_POSITION)
    drawboard.blit(chalkcloud2,CLOUD_2_POSITION)
    drawboard.blit(chalkhouse,HOUSE_POSITION)
    drawboard.blit(flower,FLOWER_POSITION)

    if honeyBeeSwitch == True :
        drawboard.blit(honeybee1, (butx, buty))
        honeyBeeSwitch = False
    else :
        drawboard.blit(honeybee2, (butx, buty))
        honeyBeeSwitch = True
    
    

    butx = a * math.cos(d*math.pi/180) + hx
    buty = a * math.cos(d*math.pi/180) * math.sin(d*math.pi/180) + hy
    d = d + 3.0
    #print(butx)
    
    
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()


    # Redraw the screen and wait a clock tick.
    pygame.display.update()
    FPSCLOCK.tick(FPS)

    
