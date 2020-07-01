# ********************************
# Python4kids: Loops
# ********************************
  
# import turtle library
import turtle

t=turtle.Turtle()

# draw a square
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)
# t.forward(100)
# t.left(90)

# use Loops
# for i in [0,1,2,3,4]:
#   print(i)

# # Draw a square inside another square box.
t.color('green')
t.speed(20)
for i in range(20):
   t.forward(i*5)
   t.right(90)

t.reset()

# for color in ["red","green","pink","blue"]:
#   print(color)
# List likes a train
# each element likes train cargo
# we can peak one cargo

# [0]-[1]-[2]-[3]-[4]-...-[N]
#
# print(colors[0])

colors=["red","green","pink","blue"]
for side in range(4):
  print("drawing side: ",side)
  mycolor = colors[side]
  print("mycolor: ",mycolor)
  t.color(mycolor)
  t.forward(100)
  t.left(90)

t.reset()

#Draw a star
t.speed(10)
t.color('red')
for i in range(5):
   t.forward(50)
   t.right(144)



# colors = [ "red","purple","blue","green","orange","yellow"]
# for x in range(60):
#    t.color(colors[x % 6])
#    t.width(x/100 + 1)
#    t.forward(x)
#    t.left(59)
 
#  # snow flakes
# import random
# colors=["red","green","pink","blue"]
# elsa = t #turtle.Turtle()
# for i in range(10):
#   print("Drawing diamond: ",i)
#   mycolor = random.choice(colors)
#   print("mycolor: ",mycolor)
#   elsa.color(mycolor)
#   elsa.forward(100)
#   elsa.right(60)
#   elsa.forward(100)
#   elsa.right(120)
#   elsa.forward(100)
#   elsa.right(60)
#   elsa.forward(100)
#   elsa.right(120)
#   elsa.right(36)


 
# turtle.reset()

# #Draw circles
# my_pen.color('blue')
# my_pen.pensize(3)

# for i in range(5):
#     my_pen.circle(i*10)
  


# #Draw a Hexagon
# my_num_sides = 6
# my_side_length = 70
# my_angle = 360.0 / my_num_sides
# for i in range(my_num_sides):
#    my_pen.forward(my_side_length)
#    my_pen.right(my_angle)

 
