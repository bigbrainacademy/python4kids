# ***************************************************************
# Making snowflakes
# ***************************************************************
# source code is originally from:
# https://projects.raspberrypi.org/en/projects/turtle-snowflakes
# ***************************************************************

 import turtle
 import random

# # multi-coloured snowflake!

# # snowflake I
 elsa = turtle.Turtle()
 wn = turtle.Screen()
 wn.bgcolor("grey")

 colors = ["red", "yellow", "blue", "green"]

 for i in range(0,10):
   for j in range(0,2):
     elsa.forward(100)
     elsa.right(60)
     elsa.forward(100)
     elsa.right(120)
   elsa.right(36)
   elsa.color(random.choice(colors))
 
 
 
# a more complicated verion of snowflake II
# elsa = turtle.Turtle()
# wn = turtle.Screen()
# wn.bgcolor("grey")

# colors = ["red", "yellow", "blue", "green"]

# elsa.penup()
# elsa.forward(90)
# elsa.left(45)
# elsa.pendown()
 
# elsa.pencolor("black")
# def branch():
#   for i in range(3):
#       for i in range(3):
#           elsa.forward(30)
#           elsa.backward(30)
#           elsa.right(45)
#       elsa.left(90)
#       elsa.backward(30)
#       elsa.left(45)
#   elsa.right(90)
#   elsa.forward(90)


# for i in range(8):
#   branch()
#   elsa.color(random.choice(colors))
#   elsa.left(45)


