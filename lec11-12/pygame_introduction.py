#Basic PyGame Program
# This program creates a window, fills the background with white, and draws a blue circle in the middle of it.
# ************************
# Simple pygame program
# ************************
# Import and initialize the pygame library
import pygame
pygame.init()

# Set up the drawing window
# uses a list to create a square window with 500 pixels on each side.
screen = pygame.display.set_mode([500, 500])

# color: (r,g,b)
red=(255,0,0)
green=(0,255,0)
blue=(0,0,255)
white=(255,255,255)
# Run until the user asks to quit
running = True
while running:
# Did the user click the window close button?
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False

  # Fill the background with white
  screen.fill(white)
   # Draw a solid blue circle in the center
  pygame.draw.circle(screen, red, (250, 250), 50)
 # Flip the display:
 # updates the contents of the display to the screen. Without this call, nothing appears in the window!
  pygame.display.flip()

# Done! Time to quit.
pygame.quit()


# Summary of pygame
# -Initialization and Modules
# -Displays and Surfaces
# The display is created using .set_mode(), which returns a Surface representing the visible part of the window. It is this Surface that you pass into drawing functions like pygame.draw.circle(), and the contents of that Surface are pushed to the display when you call pygame.display.flip().

# -Images and Rects
#   Your basic pygame program drew a shape directly onto the display’s Surface, but you can also work with images on the disk. The image module allows you to load and save images in a variety of popular formats. Images are loaded into Surface objects, which can then be manipulated and displayed in numerous ways.  Surface objects are represented by rectangles

