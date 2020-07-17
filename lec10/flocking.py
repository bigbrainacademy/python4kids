# pg template - skeleton for a new pg project
import pygame as pg
from random import randint

vec = pg.math.Vector2

WIDTH = 1024
HEIGHT = 800
FPS = 60
GRIDSIZE = 32
MOB_SIZE = 32
MOB_SPEED = 0.5
NUM_MOBS = 20
NEIGHBOR_RADIUS = 100
A_WEIGHT = 1.5
C_WEIGHT = 0.8
S_WEIGHT = 1.8

# define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)
GREEN = (0, 255, 0)
BLUE = (0, 0, 255)
YELLOW = (255, 255, 0)
LIGHTGREY = (40, 40, 40)

# initialize pg and create window
pg.init()
#pg.mixer.init()
screen = pg.display.set_mode((WIDTH, HEIGHT))
pg.display.set_caption("Spatial Hash Example")
clock = pg.time.Clock()
 
class Player(pg.sprite.Sprite):
    def __init__(self):
        pg.sprite.Sprite.__init__(self)
        self.image = pg.Surface((30, 30))
        self.image.fill(GREEN)
        self.rect = self.image.get_rect()
        self.pos = vec(WIDTH / 2, HEIGHT / 2)
        self.rect.center = self.pos

    def update(self):
        self.vel = vec(0, 0)
        self.move_8way()
        self.pos += self.vel
        self.rect.center = self.pos
        # prevent sprite from moving off screen
        if self.rect.left < 0:
            self.rect.left = 0
        if self.rect.right > WIDTH:
            self.rect.right = WIDTH
        if self.rect.top < 0:
            self.rect.top = 0
        if self.rect.bottom > HEIGHT:
            self.rect.bottom = HEIGHT

    def move_8way(self):
        keystate = pg.key.get_pressed()
        if keystate[pg.K_UP]:
            self.vel.y = -5
        if keystate[pg.K_DOWN]:
            self.vel.y = 5
        if keystate[pg.K_LEFT]:
            self.vel.x = -5
        if keystate[pg.K_RIGHT]:
            self.vel.x = 5

class Mob(pg.sprite.Sprite):
    def __init__(self):
        self.groups = all_sprites, mobs
        pg.sprite.Sprite.__init__(self, self.groups)
        self.image = pg.Surface((MOB_SIZE, MOB_SIZE))
        self.image.fill(RED)
        self.rect = self.image.get_rect()
        self.pos = vec(randint(0, WIDTH), randint(0, HEIGHT))
        self.rect.center = self.pos
        self.vel = vec(MOB_SPEED, 0).rotate(randint(0, 360))

    def flock_adjust(self):
        neighbors = 0
        self.v_a = vec(0, 0)
        self.v_c = vec(0, 0)
        self.v_s = vec(0, 0)
        for other in mobs:
            if other != self:
                if self.pos.distance_squared_to(other.pos) < NEIGHBOR_RADIUS**2:
                    self.v_a += other.vel
                    self.v_c += other.pos
                    self.v_s += other.pos - self.pos
                    neighbors += 1
                if self.pos.distance_squared_to(other.pos) < 900:
                    self.v_s += (other.pos - self.pos) * 2

        if neighbors > 0:
            self.v_a /= neighbors
            self.v_a.normalize_ip()
            self.v_c /= neighbors
            self.v_c -= self.pos
            self.v_c.normalize_ip()
            self.v_s /= neighbors
            self.v_s *= -1
            self.v_s.normalize_ip()
        return self.v_a * A_WEIGHT + self.v_c * C_WEIGHT + self.v_s * S_WEIGHT

    def find_alignment(self):
        neighbors = 0
        v = vec(0, 0)
        for other in mobs:
            if other != self:
                if self.pos.distance_squared_to(other.pos) < NEIGHBOR_RADIUS**2:
                    v += other.vel
                    neighbors += 1
        if neighbors == 0:
            return v
        else:
            v /= neighbors
            v.normalize_ip()
            return v

    def find_cohesion(self):
        neighbors = 0
        v = vec(0, 0)
        for other in mobs:
            if other != self:
                if self.pos.distance_squared_to(other.pos) < NEIGHBOR_RADIUS**2:
                    v += other.pos
                    neighbors += 1
        if neighbors == 0:
            return v
        else:
            v /= neighbors
            v -= self.pos
            v.normalize_ip()
            return v

    def find_separation(self):
        neighbors = 0
        v = vec(0, 0)
        for other in mobs:
            if other != self:
                if self.pos.distance_squared_to(other.pos) < NEIGHBOR_RADIUS**2:
                    v += other.pos - self.pos
                    neighbors += 1
        if neighbors == 0:
            return v
        else:
            v /= neighbors
            v *= -1
            v.normalize_ip()
            return v

    def update(self):
        self.dir = (player.pos - self.pos).angle_to(vec(1, 0))
        self.acc = vec(1, 0).rotate(-self.dir)

        self.acc += self.flock_adjust()
        self.acc = self.acc.normalize() * MOB_SPEED
        self.vel += self.acc
        if self.vel.length_squared() > 3**2:
            self.vel = self.vel.normalize() * 3
        self.pos += self.vel + 0.5 * self.acc
        if self.pos.x > WIDTH:
            self.pos.x = 0
        if self.pos.x < 0:
            self.pos.x = WIDTH
        if self.pos.y > HEIGHT:
            self.pos.y = 0
        if self.pos.y < 0:
            self.pos.y = HEIGHT
        self.rect.center = self.pos

all_sprites = pg.sprite.Group()
mobs = pg.sprite.Group()
player = Player()
all_sprites.add(player)
for i in range(NUM_MOBS):
    Mob()
paused = False

# Game loop
running = True
while running:
    # keep loop running at the right speed
    clock.tick(FPS)
    # Process input (events)
    for event in pg.event.get():
        # check for closing window
        if event.type == pg.QUIT:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE:
            running = False
        if event.type == pg.KEYDOWN and event.key == pg.K_SPACE:
            paused = not paused

    # Update
    player.update()
    if not paused:
        mobs.update()

    # Draw / render
    pg.display.set_caption("{:.2f}".format(clock.get_fps()))
    screen.fill(BLACK)
    #draw_grid()
    all_sprites.draw(screen)
    pg.display.flip()

pg.quit()

