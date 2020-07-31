# Import the pygame module
import pygame
import random


pygame.init()
 
WIDTH = 800
HEIGHT = 600
 
BLUE=(0,0,255)
BLACK=(0,0,0)
WHITE=(255,255,255)
 
clock = pygame.time.Clock()
screen = pygame.display.set_mode((WIDTH,HEIGHT))
  
class Player(pygame.sprite.Sprite):
  def __init__(self):
    super(Player, self).__init__()
    self.surf = pygame.image.load("jet.png").convert()
    self.surf = pygame.transform.scale(self.surf, (50, 30))
    self.surf.set_colorkey(BLACK)
    self.rect = self.surf.get_rect()
 
  def update(self, keys):
    pass
 
class Enemy(pygame.sprite.Sprite):
  def __init__(self):
    super(Enemy, self).__init__()
    self.surf = pygame.image.load("enemies.png").convert()
    #self.surf.set_colorkey(BLUE, RLEACCEL)
    self.surf.set_colorkey(BLACK)
    self.surf = pygame.transform.scale(self.surf, (10, 10))
 
    self.rect = self.surf.get_rect(
      center=(random.randint(WIDTH + 20, WIDTH + 100),random.randint(0, HEIGHT))
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
          center=(random.randint(WIDTH + 20, WIDTH + 100), random.randint(0, HEIGHT) )
          )
    # Move the cloud based on a constant speed
    # Remove the cloud when it passes the left edge of the screen
  def update(self):
    self.rect.move_ip(-5, 0)
    if self.rect.right < 0:
      self.kill()


 
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
 

  pygame.display.flip()
  # Ensure program maintains a rate of 30 frames per second
  clock.tick(30)
 

 


 
