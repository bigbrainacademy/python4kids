# Challenge Project: snake game
#
# ingredients: food, snake
#
# movement of snake:
#  --->
#   --->
#    --->
#    ...
#
# to simulate the movement of the snake,
# we clear the snake in the old position and re-draw the snake at new position. we repeat this operation many times so that the snake looks like moving forward

import turtle
import time
import random

# setup window
wn = turtle.Screen()
wn.bgcolor("grey") # color
wn.setup(400,400)  # size

# setup turtle
t = turtle.Turtle()
t.speed(0)
t.color('black')
#Set the orientation of the turtle to to_angle
t.setheading(0)
t.write('Press space to start', font=('Arial', 25, 'normal'),align='center')

# define a simple class: game
class game:
  # initialization of the variables
    started = False
    direction = 0
    tmpdir = 0
    trailpositions=[(0,0)]  # record the snake body
  # define the positions of the food
    foodpos = (random.randint(-3,3)*50,random.randint(-3,3)*50)
    score = 0
    dead = False

# define  functions to control the food and turtle
# reset food
def resetfood():
    x = random.randint(-3,3)*50
    y = random.randint(-3,3)*50
    game.foodpos = (x,y)

# change direction
def moveup():
    if game.tmpdir != 270:
        game.direction = 90
def movedown():
    if game.tmpdir != 90:
        game.direction = 270
def moveright():
    if game.tmpdir != 180:
        game.direction = 0
def moveleft():
    if game.tmpdir != 0:
        game.direction = 180


# start the game while called
def startgame():
    game.started = True
 
wn.onkey(startgame, ' ')

# check if the game is start
while not game.started:
    wn.listen() #screen events: Set focus on TurtleScreen

# move the turtle to the center
t.goto(0,0)
t.clear()
# tracer(n,delay)
# to turn turtle animation on/off and set delay for update drawings. If n is given, only each n-th regular screen update is really performed
t.tracer(0,30)

# start the game
game.started = True

# controls
wn.onkey(None, ' ')
wn.onkey(moveup, 'w')
wn.onkey(movedown, 's')
wn.onkey(moveright, 'd')
wn.onkey(moveleft, 'a')

wn.onkey(moveup, 'Up')
wn.onkey(movedown, 'Down')
wn.onkey(moveright, 'Right')
wn.onkey(moveleft, 'Left')

# make turtle visible
t.showturtle()
t.down()
t.update()
gotfood = False

# set the speed of the snake
speed = 2.0

# main part

while True:
    # clear the screen
    t.clear()

    startwait=time.time()
    currenttime=startwait

    while time.time() < startwait+(1.0/speed):
        wn.listen()
        time.sleep(0.01)

    # get the status of the turtle
    t.setheading(game.direction)
    game.tmpdir = game.direction
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
