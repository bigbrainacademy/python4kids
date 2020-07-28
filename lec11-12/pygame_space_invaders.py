# ref: https://realpython.com/pygame-a-primer/#background-and-setup
# Import the pygame module
import pygame
import time
#from pygame.locals import *

pygame.init()

# Define constants for the screen width and height
SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# colors
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)

RLEACCEL=10
# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))


# a sprite is a 2D representation of something on the screen.

# Define a Player object by extending pygame.sprite.Sprite
# The surface drawn on the screen is now an attribute of 'player'
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surf = pygame.image.load("jet.png").convert()
    self.surf = pygame.transform.scale(self.surf, (50, 30))
    #remove bg color (black)
    self.surf.set_colorkey(BLACK)

    # self.surf = pygame.Surface((75, 25))
    # self.surf.fill((255, 255, 255))
    self.rect = self.surf.get_rect()

  # Move the sprite based on user keypresses
  # use .move_ip(), which stands for move in place
  def update(self, keys):
    if keys[pygame.K_UP]:
      self.rect.move_ip(0, -5)
    if keys[pygame.K_DOWN]:
      self.rect.move_ip(0, 5)
    if keys[pygame.K_LEFT]:
      self.rect.move_ip(-5, 0)
    if keys[pygame.K_RIGHT]:
      self.rect.move_ip(5, 0)
    # Keep player on the screen
    if self.rect.left < 0:
      self.rect.left = 0
    if self.rect.right > SCREEN_WIDTH:
      self.rect.right = SCREEN_WIDTH
    if self.rect.top <= 0:
      self.rect.top = 0
    if self.rect.bottom >= SCREEN_HEIGHT:
      self.rect.bottom = SCREEN_HEIGHT


# enermies
import random

# Define the enemy object by extending pygame.sprite.Sprite
# The surface you draw on the screen is now an attribute of 'enemy'
class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super(Enemy, self).__init__()
    self.surf = pygame.image.load("enemies.png").convert()
    #self.surf.set_colorkey(BLUE, RLEACCEL)
    self.surf.set_colorkey(BLACK)
    self.surf = pygame.transform.scale(self.surf, (10, 10))

    # self.surf = pygame.Surface((20, 10))
    # self.surf.fill((255, 255, 255))

    self.rect = self.surf.get_rect(
      center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100),random.randint(0, SCREEN_HEIGHT))
      )
    self.speed = random.randint(5, 20)

# Move the sprite based on speed
# Remove the sprite when it passes the left edge of the screen
  def update(self):
    self.rect.move_ip(-self.speed, 0)
    if self.rect.right < 0:
      self.kill()

# Define the cloud object by extending pygame.sprite.Sprite
# Use an image for a better-looking sprite
class Cloud(pygame.sprite.Sprite):
  def __init__(self):
    super(Cloud, self).__init__()
    self.surf = pygame.image.load("cloud.png").convert()
    # self.surf.set_colorkey((0, 0, 0), RLEACCEL)
    self.surf.set_colorkey(BLACK)
    self.surf = pygame.transform.scale(self.surf, (100, 50))
    # The starting position is randomly generated
    self.rect = self.surf.get_rect(
          center=(random.randint(SCREEN_WIDTH + 20, SCREEN_WIDTH + 100), random.randint(0, SCREEN_HEIGHT) )
          )
    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
  def update(self):
    self.rect.move_ip(-5, 0)
    if self.rect.right < 0:
      self.kill()


# Sprite Groups:
# This is an object that holds a group of Sprite objects. So why use it? Can’t you just track your Sprite objects in a list instead? Well, you can, but the advantage of using a Group lies in the methods it exposes. These methods help to detect whether any Enemy has collided with the Player, which makes updates much easier.
# Let’s see how to create sprite groups. You’ll create two different Group objects:
#-The first Group will hold every Sprite in the game.
#- The second Group will hold just the Enemy objects.
# Create groups to hold enemy sprites and all sprites
# - enemies is used for collision detection and position updates
# - all_sprites is used for rendering

# Instantiate player. Right now, this is just a rectangle.
myplayer = Player()
enemies = pygame.sprite.Group()
clouds  = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(myplayer)

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)

ADDCLOUD = pygame.USEREVENT + 2
pygame.time.set_timer(ADDCLOUD, 1000)

# Variable to keep the main loop running
running = True
# Main loop
while running:
  # Look at every event in the queue
  for event in pygame.event.get():
    if event.type == pygame.QUIT:
      running = False
    
# Add a new enemy?
    elif event.type == ADDENEMY:
      # Create the new enemy and add it to sprite groups
      new_enemy = Enemy()
      enemies.add(new_enemy)
      all_sprites.add(new_enemy)

# Add a new cloud?
    elif event.type == ADDCLOUD:
    # Create the new cloud and add it to sprite groups
      new_cloud = Cloud()
      clouds.add(new_cloud)
      all_sprites.add(new_cloud)

# Get all the keys currently pressed
  keys = pygame.key.get_pressed()
  # Update the player sprite based on user keypresses
  myplayer.update(keys)

  # Update enemy position
  enemies.update()

  clouds.update()

# Fill the screen with sky blue
  screen.fill((135, 206, 250))
 
 # Draw all sprites
  for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)

  # # Draw the player on the screen
  # screen.blit(myplayer.surf, myplayer.rect)
  # Update the display

  # Check if any enemies have collided with the player
  # use a method called .spritecollideany(), which is read as “sprite collide any.” This method accepts a Sprite and a Group as parameters. It looks at every object in the Group and checks if its .rect intersects with the .rect of the Sprite. If so, then it returns True. Otherwise, it returns False.
  if pygame.sprite.spritecollideany(myplayer, enemies):
  # If so, then remove the player and stop the loop
    myplayer.kill()
    running = False

  pygame.display.flip()
  # Ensure program maintains a rate of 30 frames per second
  clock.tick(30)
 


def text_objects(text, font):
    textSurface = font.render(text, True, BLACK)
    return textSurface, textSurface.get_rect()

def message_display(text):
    largeText = pygame.font.Font('freesansbold.ttf',115)
    TextSurf, TextRect = text_objects(text, largeText)
    TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
    screen.blit(TextSurf, TextRect)

    pygame.display.update()

    time.sleep(20)
       

def game_over():
    message_display('Game over')

game_over()


 
