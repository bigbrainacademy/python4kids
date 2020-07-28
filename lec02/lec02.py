## **************************************************
## *                Python4kids                     *
## **************************************************
## *         lecture02: Programming with turtle     *
## **************************************************
## We are going to learn:
## **************************************************
# - What is the Python turtle library
# - Program with the Python turtle library
# - Grasp some important Python concepts and turtle commands
# - Develop a short entertaining game
## **************************************************
##  Basics
## **************************************************
# - Moving the Turtle
# - Drawing a Shape
# - Drawing Preset Figures
# - Changing the Screen Color
# - Changing the Screen Title
# - Changing the Turtle Size
# - Changing the Pen Size
# - Changing the Turtle and Pen Color
# - Filling in an Image
# - Changing the Turtle Shape
# - Changing the Pen Speed
# - Clearing the Screen
## **************************************************
## * Challenge
## **************************************************
# Using Loops and Conditional Statements
# for Loops
# while Loops
# Conditional Statements
## **************************************************
# Final Project: The Python Turtle Race
## **************************************************
# Setting Up the Game Environment
# Setting Up the Turtles and Homes
# Creating the Die
# Developing the Game
## **************************************************
 
# Let's firt import the Python turtle library
# (a library is a set of important functions and methods that you can access to make your programming easier.)

import turtle

t = turtle.Turtle()
# The turtle is like a pen, you can set pencolor
t.pencolor('red')
# change the color of the turtle
t.fillcolor("purple")

# you can set a shape for the pen
t.shape("turtle")   # "arrow", "circle")

# Now let's draw lines by moving the turtle
t.forward(100)   # length of 100 units
t.left(90)       #  angle of 90 degree
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)

# clear the screen
t.clear()

# Excellent! You have drawn a square

# Drawing a circle
t.pencolor('blue')
t.circle(50)  # radius of the circle
 

# Filling in an Image
t.begin_fill()
t.fillcolor("green")
t.circle(-50)   # put minus sign to circle in clockwise direction
t.end_fill()

# Changing the Pen Speed
t.speed(100)
t.circle(50,180) # (radius, degree)
t.circle(100)


# put all the parameters together
t.en(pencolor="purple", fillcolor="orange", pensize=10, speed=100)
t.begin_fill()
t.circle(100)
t.end_fill()

# introduce variables

# side = 100 # distance
# angle= 90
# t.forward(side)
# t.left(angle)
# t.forward(side)
# t.left(angle)
# t.forward(side)
# t.left(angle)
# t.forward(side)
# t.left(angle)

# introduce the concept of loop
# draw many squares with different sides
 
#angle= 90

# # one small square
# side = 50
# t.forward(side)
# t.left(angle)
# t.forward(side)
# t.left(angle)
# t.forward(side)
# t.left(angle)
# t.forward(side)
# t.left(angle)
 

# Can we make the code simpler?
# use for loop

# for side in [50,100,150]:
#   t.forward(side)
#   t.left(angle)
#   t.forward(side)
#   t.left(angle)
#   t.forward(side)
#   t.left(angle)
#   t.forward(side)
#   t.left(angle)


# # is it possible to make the above code even simpler?
# side=50
# for loop in [1,2,3,4]:
#   t.forward(side)
#   t.left(angle)
# side=100
# for loop in [1,2,3,4]:
#   t.forward(side)
#   t.left(angle)

# here we go !
# for side in [50,100,150]:
#   for loop in [1,2,3,4]:
#       t.forward(side)
#       t.left(angle)


# [1,2,3,4] can be simply given by range(1,5)
# Attention: range(a,b)=a,a+1,..,b-1 (NOT b)
# ranges = range(1,5)
# print(ranges)

# for side in [50,100,150]:
#   for loop in range(1,5):
#     t.forward(side)
#     t.left(angle)

 

 # Change we also change the angle?

# triangle
# for loop in range(1,4):
#   side =  50
#   angle = 360/3
#   print('side=',side)
#   t.forward(side)
#   t.left(angle)


# pentagon
# for loop in range(1,6):
#   side =  50
#   angle = 360/5
#   print('side=',side)
#   t.forward(side)
#   t.left(angle)

# # hexagon
# for loop in range(1,7):
#   side =  50
#   angle = 360/6
#   print('side=',side)
#   t.forward(side)
#   t.left(angle)

 

# for radius in [10,20,30,40,50,60,70,80,90]:
#   t.circle(radius)

# challenge project
 

# # Set up the screen
# wn = turtle.Screen()
# wn.bgcolor("black")
 
# colors = ["red", "yellow", "blue", "green"]
# for x in range(50):
#     color_number = x%4   # mode
#     print(color_number)
#     t.pencolor(colors[color_number])
#     t.forward(2*x)
#     t.left(91)

 
# t.pencolor("black")
# colors = ["red", "yellow", "blue", "green"]

# for x in range(10,1,-1):
#   color_number = x%4
#   t.fillcolor(colors[color_number])
#   t.begin_fill()
#   t.circle(x*10)
#   t.end_fill()
 
