#GuessingGame.py

import random

# generate a random number in between 1 and 10
the_number = random.randint(1, 10)

# guess a number using input()
# attention: here your_guess is a string!
your_guess = input("Guess a number between 1 and 10: ")

# we need to convert the string to integer number using int()
guess = int(your_guess)

# check if you did a right guess or not
while guess != the_number:
    if guess > the_number:
        print(guess, "was too high. Try again.")
    if guess < the_number:
        print(guess, "was too low. Try again.")
        
    guess = int(input("Guess again: "))
    
print(guess, "was the number! You win!") 
  
