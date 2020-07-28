# Math game
import random

print("Welcome to MATH WORLD!")


q1 = "Do you want to do addition or multiplication? \n (enter 1 for addition and 2 for multiplication) \n"

operation = input(q1)
while operation != '1' and operation != '2':
  operation = input(q1)

condition=True

if operation == '1':
  while condition:
    num1 = random.randrange(1, 101)
    num2 = random.randrange(1, 101)
    add12 = num1 + num2

    your_answer=input("What's "+str(num1)+'+'+str(num2)+"? \n")
    if int(your_answer)==add12:
      condition=False
      print("Bingo! You are right!")
    else:
      print("Oho, try again.")


 
if operation == '2':
  while condition:
    num1 = random.randrange(1, 10)
    num2 = random.randrange(1, 10)
    mul12 = num1 * num2

    your_answer=input("What's "+str(num1)+'*'+str(num2)+"? \n")
    if int(your_answer)==mul12:
      condition=False
      print("Bingo! You are right!")
    else:
      print("Oho, try again.")
