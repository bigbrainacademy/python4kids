###########################
# LearnToCode4Kids: Pygame
###########################
#
#  - create a playable game and discover how the pygame framework
#    lets you work with graphics and sound.
#  - create game objects: sprites
#  - “game loop” that repeatedly updates and draws items on the screen
#  - use the event mechanism of pygame to capture keyboard input,
#    and use events to control an object on the screen.
#  - implement a start screen and a game screen to make a complete game experience.

#  import the pygame module, and one can use the functions and classes it contains.

# sys module

import sys
import pygame


# initialize the pygame
# use the init() function sets up the different pygame elements,
# returns a tuple that tells you how many elements have been successfully initialized,
# and how many have failed to initialize
pygame.init()

# frames per second
FPS = 60

# setup screen size
# The size is given in pixels (a pixel is the size of a dot on the display).
# The more pixels you have, the better quality the display.
#  We’ll use a screen size of 800 pixels wide and 600 pixels high.
width=800
height=600
size=(width,height)

# creates a pygame drawing surface
win = pygame.display.set_mode(size)


# change the title of the drawing window
pygame.display.set_caption("My first pygame project")


 # specify color
# The color of an item in pygame is expressed as a tuple containing three values.
# Each value in the tuple (r, g, b) represents the amount of red, green, and blue, respectively.
# The lowest level is 0; the highest level is 255.
# If we want to draw a red line, we can create a tuple that contains all the red and none of the other two primary colors
 
 
red     = (255,0,0)
white   = (255,255,255)
black   = (0,0,0)
yellow  = (255, 255, 0)
magenta = (255, 0, 255)
cyan    = (0, 255, 255)
 
# set background color
win.fill(white)

clock = pygame.time.Clock()

# specify position
#
# (0,0) ---------------------------------> x
#     |
#     |
#     |
#     |           +(x,y)
#     |
#     |
#     |
#     |
#     |
#     v
#    y
#
#   - For a given position on the screen, the value of x specifies how far the position is from the left edge, and the value of y specifies how far down the screen from the top edge.
#   - A specific location is expressed as a tuple containing the values (x, y). The figure below shows how pygame coordinates work.
#   - The origin, which is the point with the coordinate (0,0) is the top left corner of the display.
#   - Increasing the value of x moves you toward the right of the screen, and increasing the value of y will move you down the screen.

  

box_x = 300
box_y = 300
position = (box_x,box_y)

game_run = True

while game_run:
     # The tick method will pause the game until the start of the next frame “slot.”. The value is larger, the faster the object will move.
   
   clock.tick(FPS)
   #pygame.time.delay(50)  # mini second
   for event in pygame.event.get():
       if event.type == pygame.QUIT:
           game_run = False
       # inputs from key board
       
       keys = pygame.key.get_pressed()
        
       if keys[pygame.K_LEFT]:
           box_x -= 25
       elif keys[pygame.K_RIGHT]:
           box_x += 25
       elif keys[pygame.K_UP]:
           box_y -= 25
       elif keys[pygame.K_DOWN]:
           box_y += 25
       
       # press SPACE to quite the game
       elif keys[pygame.K_SPACE]:
           game_run= False

       # you can try by comment the following line
       win.fill(white)
       
       pygame.draw.rect(win,black,[box_x,box_y,25,25])
       
       pygame.display.update()
       


pygame.quit()

# The exit method is in the sys module
# Call the exit() function to exit a Python program instantly
sys.exit()
