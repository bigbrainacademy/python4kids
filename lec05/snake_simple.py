import turtle
import time
import random

wn = turtle.Screen()
wn.bgcolor("grey")

wn.setup(400,400)

t = turtle.Turtle()
t.speed(0)
    
# define a class
class game:
  # initialization of the variables
    started = False
    direction = 0
    tmpdir = 0
    trailpositions=[(0,0)]
  # define the positions of the food
    foodpos = (random.randint(-3,3)*50,random.randint(-3,3)*50)
    score = 0
    dead = False

# reset food
def resetfood():
    game.foodpos = (random.randint(-3,3)*50,random.randint(-3,3)*50)

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


# swith
def startgame():
    game.started = True
 
 
t.color('black')
#Set the orientation of the turtle to to_angle
t.setheading(0)
t.write('Press space to start', font=('Arial', 25, 'normal'),align='center')

wn.onkey(startgame, ' ')

# check if the game is start
while not game.started:
    wn.listen()

#
t.goto(0,0)
t.clear()
# tracer(n,delay)
# to turn turtle animation on/off and set delay for update drawings. If n is given, only each n-th regular screen update is really performed
t.tracer(0,30)
game.started = True

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
speed = 2.0

while True:
    t.clear()

    startwait=time.time()
    currenttime=startwait
    while time.time() < startwait+(1.0/speed):
        wn.listen()
        time.sleep(0.01)

    t.setheading(game.direction)
    game.tmpdir = game.direction
    t.forward(50)
    pos=t.pos()
    pos = (round(pos[0]/50)*50,round(pos[1]/50)*50)
    t.goto(pos)
    game.dead = False

    if pos in game.trailpositions:
        game.dead = True

    if pos == game.foodpos:
        resetfood()
        gotfood = True
        speed += 0.1
        game.score += 1

    #print('pos',pos)
    t.up()
    t.goto(game.trailpositions[0])
    t.down()
    for pos2 in game.trailpositions:
        t.goto(pos2)
    t.up()
    
    t.goto(game.foodpos)
    t.dot(4)
    
    
    t.goto(pos)
    
    if not gotfood:
        del game.trailpositions[0]

    game.trailpositions.append(pos)

    t.goto(0,100)
    t.write('Score: '+str(game.score), font=('Arial', 15, 'normal'),align='center')
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
