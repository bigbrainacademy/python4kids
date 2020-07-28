# building a house
import turtle

t = turtle.Turtle()
# pen up
t.penup()
t.goto(0,-100)


t.pendown()
t.speed(100)

# plot a small square
t.pencolor("red")
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)
t.forward(50)
t.left(90)

# plot a big square
t.pencolor("black")
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(150)
t.left(90)
t.forward(100)
t.left(90)
t.forward(50)

# pen up
t.penup()
t.goto(100,0)
t.pendown()
t.pencolor("green")
t.left(120)
t.forward(150)
t.left(120)
t.forward(150)

t.penup()
t.goto(500,500)
