# project: turtle race with steps determined by rolling a die

import turtle
import random

# setting for referee

t = turtle.Turtle()
t.color("black")
t.speed(100)

t.penup()
t.goto(0,200)
t.pendown()
t.write("Turtle race",font=('Courier',30,'italic'),align='center')
t.penup()
t.goto(0,1000)

# setting for player one
player_one = turtle.Turtle()
player_one.shape("turtle")
player_one.color("blue")
player_one.speed(10)


# setting for player two
player_two = turtle.Turtle()
player_two.shape("turtle")
player_two.color("red")
player_two.speed(10)



# marking destination with a circle
player_one.penup()
player_one.goto(200,80)
player_one.pendown()
player_one.circle(20)

player_two.penup()
player_two.goto(200,-120)
player_two.pendown()
player_two.circle(20)

# move the players to the starting line

player_one.penup()
player_one.goto(-200,100)

player_two.penup()
player_two.goto(-200,-100)
 

# The steps of each turtle are determined by rolling a dice

die=[1,2,3,4,5,6]

player_one.pendown()
player_two.pendown()

# referee
t.penup()
t.goto(0,-200)
t.pendown()

while True:

  # recording the x-position of each turtle
  player_one.write(player_one.pos()[0]+200)
  player_two.write(player_two.pos()[0]+200)

  if(player_one.pos() >=(180,100)):

    t.write("Player one win !",font=('Courier',30,'italic'),align='center')
    break
  elif(player_two.pos() >=(180,-100)):
    t.write("Player two win !",font=('Courier',30,'italic'),align='center')
    break
  else:
    player_one_turn = input("Player one's turn. Press 'Enter' to roll the die ")
    die_outcome = random.choice(die)
    print("The result of the die roll is: ", die_outcome)
    print("The number of steps will be: ",20*die_outcome)
    player_one.forward(20*die_outcome)


    player_two_turn = input("Player two's turn. Press 'Enter' to roll the die ")
    die_outcome = random.choice(die)
    print("The result of the die roll is: ", die_outcome)
    print("The number of steps will be: ",20*die_outcome)
    player_two.forward(20*die_outcome)

 

t.penup()
t.goto(0,-1000)
