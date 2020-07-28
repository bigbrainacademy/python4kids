# ref: https://realpython.com/pygame-a-primer/#background-and-setup
# Import the pygame module
import pygame
import time

pygame.init()

SCREEN_WIDTH = 800
SCREEN_HEIGHT = 600

# colors
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
 
# Setup the clock for a decent framerate
clock = pygame.time.Clock()

# Create the screen object
# The size is determined by the constant SCREEN_WIDTH and SCREEN_HEIGHT
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))

class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surf = pygame.Surface((75, 25))
    self.surf.fill((255, 255, 255))
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

    self.surf = pygame.Surface((20, 10))
    self.surf.fill(WHITE)
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
 
myplayer = Player()
enemies = pygame.sprite.Group()
all_sprites = pygame.sprite.Group()
all_sprites.add(myplayer)

# Create a custom event for adding a new enemy
ADDENEMY = pygame.USEREVENT + 1
pygame.time.set_timer(ADDENEMY, 250)
 
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
 
# Get all the keys currently pressed
  keys = pygame.key.get_pressed()
  # Update the player sprite based on user keypresses
  myplayer.update(keys)
  # Update enemy position
  enemies.update()

#  clouds.update()

# Fill the screen with sky blue
  screen.fill((135, 206, 250))
  #screen.fill((0, 0, 0))
 
 # Draw all sprites
  for entity in all_sprites:
    screen.blit(entity.surf, entity.rect)
    
 # Draw all sprites
#
  # Draw the player on the screen
  #screen.blit(myplayer.surf, myplayer.rect)

  # Update the display
 # Flip everything to the display
  pygame.display.flip()
 


# def text_objects(text, font):
#     textSurface = font.render(text, True, BLACK)
#     return textSurface, textSurface.get_rect()

# def message_display(text):
#     largeText = pygame.font.Font('freesansbold.ttf',115)
#     TextSurf, TextRect = text_objects(text, largeText)
#     TextRect.center = ((SCREEN_WIDTH/2),(SCREEN_HEIGHT/2))
#     screen.blit(TextSurf, TextRect)

#     pygame.display.update()

#     time.sleep(20)
       

# def game_over():
#     message_display('Game over')

# game_over()


 
