# project: snake

import turtle
import random
import time

# set up window
wn = turtle.Screen()
wn.bgcolor("grey")
wn.setup(400,400)

# set up the turtle
t = turtle.Turtle()
t.speed(0)
t.color('black')
# set up turtle heading
t.setheading(0)
t.penup()
#t.goto(-100,0)
t.write("Press space to start", font=('Arial',20,'normal'), align='center')

# define a simple class: game

class game:

  # initializing some variables
  start     = False
  direction = 0  # degree
  temdir    = 0 # degree
  # generate a coordinates for the food randomly
  foodpos = (random.randint(-3,3)*50, random.randint(-3,3)*50)
  # record the body of the snake
  trailpositions =[(0,0)]
  score = 0
  dead  = False


# define a function to control the position of new food
def resetfood():
  x = random.randint(-3,3)*50
  y = random.randint(-3,3)*50
  game.foodpos = (x,y)

# define controling functions
def moveup():
  if game.temdir !=270:
    game.direction = 90

def movedown():
  if game.temdir !=90:
    game.direction = 270

def moveleft():
  if game.temdir !=0:
    game.direction = 180

def moveright():
  if game.temdir !=180:
    game.direction = 0

# start the game while called

def startgame():
  game.start = True

wn.onkey(startgame,' ')

# check if the game starts
while not game.start:
  wn.listen()

# move the turtle to the center
t.goto(0,0)
t.clear()
t.tracer(0,30)

# start the game
game.start = True

# controls
wn.onkey(moveup, 'Up')
wn.onkey(movedown,'Down')
wn.onkey(moveleft,'Left')
wn.onkey(moveright,'Right')
wn.onkey(None,' ')

# make turtle visible
t.showturtle()
t.down()
t.update()
gotfood = False

# set the speed of the snake
speed = 2

# Game loop

while True:
  t.clear()

  start_wait  =time.time()
  current_time=start_wait

  while time.time() < start_wait + (1.0/speed):
    wn.listen()
    time.sleep(0.01)




  # get the status of the turtle
  t.setheading(game.direction)
  game.temdir = game.direction
  # move forward by 50 units along the current direction
  t.forward(50)
  pos=t.pos() # get current position
  # round the current position to multiples of 50
  # pos[0] is x, pos[1] is y
  pos = (round(pos[0]/50)*50,round(pos[1]/50)*50)
  t.goto(pos)
  game.dead = False

  #print(game.trailpositions)
  # check if the snake head touch its body
  if pos in game.trailpositions:
      game.dead = True

  # check if the turtle touch the food
  if pos == game.foodpos:
      resetfood()
      gotfood = True
      speed += 0.1
      game.score += 1

  
  t.up()
  # move the pen to the tail of the snake
  t.goto(game.trailpositions[0])
  t.down()
  # starting from the tail of the snake, draw the body of the snake using goto() method
  for pos2 in game.trailpositions:
      t.goto(pos2)

  # draw the food using dot() at the foodpos position
  t.up()
  t.goto(game.foodpos)
  t.dot(4) # size of the dot
  
  # simulating the movement of the snake by deleting the tail and drawing the head
  # see below:
  #.    tail body head
  #. t1: - - - ->
  #. t2    - - - ->
  #. t3      - - - ->
  # .....
  # if the snake touches the food, keep the tail
  t.goto(pos)
  if not gotfood:
      del game.trailpositions[0]

  # save the current position into trailpositions
  game.trailpositions.append(pos)

  # reprint out score
  t.goto(150,150)
  t.write('Score: '+str(game.score), font=('Arial', 15, 'normal'),align='right')
  t.goto(pos)

  t.update()
  gotfood = False

# dead if touch the walls
  if pos[0] >= 200:
      game.dead = True
  elif pos[0] <= -200:
      game.dead = True
  elif pos[1] >= 200:
      game.dead = True
  elif pos[1] <= -200:
      game.dead = True

  if game.dead:
      break


  
  t.down()





