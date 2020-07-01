## **************************************
## *    Python4kids                     *
## **************************************
## *  starwars+guessing number project  *
## **************************************

# put all the sentences that R2D2 are going to say here
# introduce variables s1, s2, ..., to store these sentences
 
s1 = "R2D2: Welcome to Star Wars!"
q2 = "R2D2: What's your name? \n "
s3 = "R2D2: Hi,"
s4 = "R2D2: I hope you are doing well today."
q5 = "R2D2: How old are you? (enter a number) \n"
s6 = "R2D2: Wow! Next year you will be "
s7 = "R2D2: Let's fight Darth Vader together!"
s8 = "Why don't we play a guess game to decide who will win? \n"

# let's talk with R2D2 by using print() and input() methods

print(s1)
# use input() for questions
name = input(q2)
print(s3,name)
print(s4)
# use input() for questions
str4age=input(q5)
# here age is a string. we need to convert it to a number using int() representing integer
thisYear = int(str4age)
# let's add 1 to the num4age
nextYear = thisYear + 1
# convert the number back to string
str4nextYear = str(nextYear)
print(s6+str4nextYear+' year old!') # we can add strings

print(s7)
print(s8)
 

# Below is for the guessing part
import random
 
# generate a random number in between 1 and 10
secret_number = random.randint(1, 10)

# guess a number using input()
# attention: here your_guess is a string!
your_guess = input("Guess a secret number between 1 and 10: ")

# we need to convert the string to integer number using int()
guess = int(your_guess)

# check if you did a right guess or not
while guess != secret_number:
    if guess > secret_number:
        print(guess, "was too high. Try again.")
    if guess < secret_number:
        print(guess, "was too low. Try again.")
        
    guess = int(input("Guess again: "))
    
print(guess, "was the number! You win!")
 
