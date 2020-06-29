## **************************************************
## *                Python4kids                     *
## **************************************************
## *          lecture01: starwars project           *
## **************************************************
## We are going to learn:
## - how to use comments, change line, etc
## - how to use input() and print() functions
## - how to define string and integer numbers
## - how to join two strings and manipulate numbers
## - how to use if...else...
## **************************************************
 

import time


print("R2D2: Welcome to Star Wars!")

# name=input("R2D2: What's your name? \n")
# # - don't forget qotation mark "" for a string
# # - \n is used for change line
# print("R2D2: Hi, "+name+"!")
# print("R2D2: I hope you are doing well today.")
## - The operator + is for joining two strings.
# **********************************************************
# Now let's try to repeat the above operation with variables
# **********************************************************

R2D2_S1 = "R2D2: What's your name? \n >>>"
name    = input(R2D2_S1)

# Luke Skywalker.
# Leia Organa.
# Ben Solo.

R2D2_S2 = "R2D2: Hi, "+ name+"!"
R2D2_S3 = "R2D2: I hope you are doing well today."

print(R2D2_S2)
print(R2D2_S3)


## Now let's add some more information

age = input("R2D2: How old are you? (pls enter a number)\n >>>")
next_year_age = int(age) + 1

R2D2_S4="R2D2: Wow! Next year you will be "+str(next_year_age)+" years old."
print(R2D2_S4)

weapon=input("R2D2: What kid of weapons do you want to choose?\n >>>")

# lightsaber

R2D2_S4="R2D2: Good choice! Your weapon "+str(weapon)+" is really cool!"
print(R2D2_S4)


R2D2_S5="R2D2: Let's fight Darth Vader together!"
print(R2D2_S5)


print("Why don't we play a guess game to decide who will win? \n")

# question
question="Can you guess what I am? \n I am living in China.\
\n I am a kind of bear. \
\n I am black and white. \
\n I eat bamboo.\n >>> "

time.sleep(2)   # Delays for 5 seconds.


print("\n")

animal=input(question)

R2D2_S6=" Congratulation! You win!"
R2D2_S7=" Sorry! I am Panda!"

if animal !="Panda" and animal !="panda":
  print(R2D2_S7)
else:
  print(R2D2_S6)

 
