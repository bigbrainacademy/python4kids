# ************************
#  Python4kids:  Strings
# ************************
#
# In this example, the concepts of
# variables, strings,
# will be introduced.

# source: https://www.w3schools.com/python/python_strings.asp

# what's string in python?
# surrounded by either single quotation marks, or double quotation marks.

# example:
# 'hello', "hello".


# define a string
str1 = "Hello"
str2 = 'Welcome'

# print out a string
print(str1)
print(str2)



# Multiline Strings

multiline_str= \
""" Hello!
My name is Jim.
How are you doing today?"""

print(multiline_str)




# String Concatenation: To concatenate, or combine, two strings you can use the + operator.

str12 = str1+str2
print(str12)






# Slicing a string

longStr  = 'Minecraft is a sandbox video game developed by Mojang. Minecraft was created by Markus "Notch" Persson in the Java programming language and was released as a public alpha for personal computers in 2009 before officially releasing in November 2011, with Jens Bergensten taking over development around then. It has since been ported to various platforms and is the best-selling video game of all time, with 180 million copies sold across all platforms and 112 million monthly active users as of 2019.'

print(longStr[0:55])



# Check String
# Check if the phrase "video gam" is present in the string: longStr
 
x = "video" in longStr # return True/False
print(x)





# string format

# 1) cannot combine a string with a number

str1 = "my age is"
age = 10

#print(str1+age)


print(str1+' {}'.format(age))

quantity = 3
itemno = 567
price = 49.95
myorder = "I want to pay {2} dollars for {0} pieces of item {1}."
print(myorder.format(quantity, itemno, price))



# Escape Character: a backslash \ followed by the character you want to insert.
txt = "We are the so-called \"Vikings\" from the north."
print(txt)


# String Methods
#
#Method    Description
#capitalize()    Converts the first character to upper case
#casefold()    Converts string into lower case
#center()    Returns a centered string
#count()    Returns the number of times a specified value occurs in a string
#encode()    Returns an encoded version of the string
#endswith()    Returns true if the string ends with the specified value
#expandtabs()    Sets the tab size of the string
#find()    Searches the string for a specified value and returns the position of where it was found
#format()    Formats specified values in a string
#format_map()    Formats specified values in a string
#index()    Searches the string for a specified value and returns the position of where it was found
#isalnum()    Returns True if all characters in the string are alphanumeric
#isalpha()    Returns True if all characters in the string are in the alphabet
#isdecimal()    Returns True if all characters in the string are decimals
#isdigit()    Returns True if all characters in the string are digits
#isidentifier()    Returns True if the string is an identifier
#islower()    Returns True if all characters in the string are lower case
#isnumeric()    Returns True if all characters in the string are numeric
#isprintable()    Returns True if all characters in the string are printable
#isspace()    Returns True if all characters in the string are whitespaces
#istitle()    Returns True if the string follows the rules of a title
#isupper()    Returns True if all characters in the string are upper case
#join()    Joins the elements of an iterable to the end of the string
#ljust()    Returns a left justified version of the string
#lower()    Converts a string into lower case
#lstrip()    Returns a left trim version of the string
#maketrans()    Returns a translation table to be used in translations
#partition()    Returns a tuple where the string is parted into three parts
#replace()    Returns a string where a specified value is replaced with a specified value
#rfind()    Searches the string for a specified value and returns the last position of where it was found
#rindex()    Searches the string for a specified value and returns the last position of where it was found
#rjust()    Returns a right justified version of the string
#rpartition()    Returns a tuple where the string is parted into three parts
#rsplit()    Splits the string at the specified separator, and returns a list
#rstrip()    Returns a right trim version of the string
#split()    Splits the string at the specified separator, and returns a list
#splitlines()    Splits the string at line breaks and returns a list
#startswith()    Returns true if the string starts with the specified value
#strip()    Returns a trimmed version of the string
#swapcase()    Swaps cases, lower case becomes upper case and vice versa
#title()    Converts the first character of each word to upper case
#translate()    Returns a translated string
#upper()    Converts a string into upper case
#zfill()    Fills the string with a specified number of 0 values at the beginning

# an example
str='hello, world!'
print(str.upper())


# project
# let's build a vocabulary !
