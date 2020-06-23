
# **********************************************************
## lecture01: first python code
# **********************************************************
## - practice with the input() function
## - concept of variables: string and integer number
## - proactice with print() function


print("R2D2: Welcome to Star Wars!")

# name=input("R2D2: What's your name? \n")

# # - don't forget qotation mark "" for a string
# ## - \n is used for change line

# print("R2D2: Hi, "+name+"!")
# print("R2D2: I hope you are doing well today.")

## - The operator + is for joining two strings.


# **********************************************************
# Now let's try to repeat the above operation with variables
# **********************************************************

R2D2_S1 = "R2D2: What's your name? \n"

name    = input(R2D2_S1)

R2D2_S2 = "R2D2: Hi, "+ name+"!"
R2D2_S3 = "R2D2: I hope you are doing well today."

print(R2D2_S2)
print(R2D2_S3)


## Now let's add some more information
age = input("R2D2: How old are you? \n")
next_year_age = int(age) + 1

R2D2_S4="R2D2: Wow! Next year you will be "+str(next_year_age)+" years old."
print(R2D2_S4)

R2D2_S5="R2D2: Congratulation! Let's fight Darth Vader together!"
print(R2D2_S5)
 



