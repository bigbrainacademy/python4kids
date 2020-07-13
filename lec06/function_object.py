# ***********************
# Python4kids
# ***********************
# we will learn:
# - basic concept of Functions and Objects
# - how to define a function
# - how to pass arguments
# - implementation of functions into Turtle

# def my_function(name):
#   print("Hi," + name)
# my_function("Alice")

# def apples(color,number):
#   print("I want "+str(number)+' '+color+" apples.")
# apples('red',4)

# def add(a,b):
#   return a+b

# def multiply(a,b):
#   return a*b

# print("3+5=",add(3,5))
# print("3*5=",multiply(3,5))


# def gauss_sum(start,stop):
#   sum = 0
#   for num in range(start,stop+1):
#     sum +=num
#   return sum

# print("1+2+...+10=",gauss_sum(1,10))
# print("1+2+...+100=",gauss_sum(1,100))

 
# class and object
# Create a class named mystudent, with a property named: age,name,grade
class mystudent:
  age = 0
  name ='Jack'
  grade=0

# Now we can use the class named mystudent to create objects
Alice = mystudent() # no arguments
Alice.age=12
Alice.name="Alice"
Alice.grade=7
print(Alice.name)
print(Alice.age)
print(Alice.grade)

#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#The examples above are classes and objects in their simplest form, and are not really useful in real life applications.
#To understand the meaning of classes we have to understand the built-in __init__() function.
#All classes have a function called __init__(), which is always executed when the class is being initiated.
#Use the __init__() function to assign values to object properties, or other operations that are necessary to do when the object is being created:

# create a class: student
class student:
  # pass arguments: name,age,grade
  def __init__(self,name,age,grade):
    self.name=name
    self.age = age
    self.grade = grade
    
    # create a method (methods in objects are functions that belong to the object.)
   def myname(self):
        print("My name is "+self.name)

# create an object Alice
Alice = student("Alice",8,3)
# access the information
print(Alice.name+' is '+str(Alice.age)+' years old.')

# use the method myname in the objet Alice
Alice.myname()



class mymath:
  def __init__(self,num1,num2):
    self.num1 = num1
    self.num2 = num2

  # create methods: add and multiply
  def add(self):
    return self.num1+self.num2

  def multiply(self):
    return self.num1*self.num2

# create an object
calculator = mymath(0,0)
# modify the values of num1 and num2
calculator.num1 = 3
calculator.num2 = 4
print(calculator.add())
print(calculator.multiply())



# Math game
# import random

# print("Welcome to MATH WORLD!")


# q1 = "Do you want to do addition or multiplication? \n (enter 1 for addition and 2 for multiplication) \n"

# operation = input(q1)
# while operation != '1' and operation != '2':
#   operation = input(q1)

# condition=True

# if operation == '1':
#   while condition:
#     num1 = random.randrange(1, 101)
#     num2 = random.randrange(1, 101)
#     # call the function add()
#     add12 = add(num1,num2)

#     your_answer=input("What's "+str(num1)+'+'+str(num2)+"? \n")

#     if int(your_answer)==add12:
#       condition=False
#       print("Bingo! You are right!")
#     else:
#       print("Oho, try again.")


 
# if operation == '2':
#   while condition:
#     num1 = random.randrange(1, 10)
#     num2 = random.randrange(1, 10)
#     # call the function multiply()
#     mul12 = multiply(num1,num2)

#     your_answer=input("What's "+str(num1)+'*'+str(num2)+"? \n")
#     if int(your_answer)==mul12:
#       condition=False
#       print("Bingo! You are right!")
#     else:
#       print("Oho, try again.")

