#!/usr/bin/env python3

"""
4c64a46eed6e708ab2c67000af803568
python
lab3
v2
lobe16
2017-09-15 14:25:50
v2.3.3 (2017-06-12)

Generated 2017-09-15 16:25:51 by dbwebb lab-utility v2.3.3 (2017-06-12).
https://github.com/mosbth/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 3 - python
#
# In these exercises we will work with functions.
#



# --------------------------------------------------------------------------
# Section 1. Functions
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a function called `greeter` that returns `"Hi, the weather is nice
# today!"`.
#
# Answer with the return value from a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#

def greeter():
    """
    A function that says the weather is nice
    """
    return "Hi, the weather is nice today!"


ANSWER = greeter()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Assign the words: 'pringles' and 'lollipop' to two different variables.
#
# Create a function and pass the two words as arguments to it. Your function
# should return them as a single word.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

firstWord = "pringles"
secondWord = "lollipop"

def combineTwoWords(word1, word2):
    """
    A function concatenates two words
    """
    return word1 + word2

ANSWER = combineTwoWords(firstWord, secondWord)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a function called `funny_word` that takes one argument and prepends
# it to the string ' is a funny word'. **EXAMPLE:** If the argument is
# 'water', the function should return: `"water is a funny word"`.
#
# Use the argument 'beverage' and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#
def funny_word(word):
    """
    A function that prepends a word to another string
    """
    return word + " is a funny word"

ANSWER = funny_word("beverage")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a function called `summation` that takes two arguments. The function
# should return the sum of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 7 and 34.
#
# Write your code below and put the answer into the variable ANSWER.
#

def summation(arg1, arg2):
    """
    A function that returns the sum of two arguments
    """
    return arg1 + arg2




ANSWER = summation(7, 34)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a function called `multiplication` that takes two arguments. The
# function should return the product of the two arguments.
#
# Answer with the return value from a call to the function with the two
# arguments 7 and 34.
#
# Write your code below and put the answer into the variable ANSWER.
#

def multiplication(arg1, arg2):
    """
    A function that takes two arguments and returns the product of the two
    """
    return arg1 * arg2


ANSWER = multiplication(7, 34)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Create a function called `in_range` that takes one argument. The function
# should return `True` if the argument is higher than 50 and lower than 100.
# If the number is out of range, the function should return `False`. The
# return type should be boolean.
#
# Use the argument 98 and answer with a call to the function.
#
# Write your code below and put the answer into the variable ANSWER.
#
def in_range(value):
    """
    A function that takes a value and compares it with 50 and 100
    If 50 < value < 100, then it returns true
    """
    if value > 50 and value < 100:
        return True
    return False

ANSWER = in_range(98)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Create a function called `multiplicator`. Inside the function create a loop
# that iterates from 4 to 15 (both included). For each number use the
# `multiplication` function from above to get the square of the current
# number. The function should return a comma-separated string of the squared
# numbers,  without an ending `,`.
#
# Answer with a call to the function `multiplicator`.
#
# Write your code below and put the answer into the variable ANSWER.
#

def multiplicator(low, high):
    """
    A function that returns comma-separated squares of values
    It calculates squares of values using the multiplication() function above
    """
    string = ""
    for num in range(low, high):
        string += (str(multiplication(num, num)) + ",")
    return string[:-1]
# multiplicator()
# def multipl(a, b):
#     """
#     loopig 5-19 and checking the square of each,
#     returning them all in a comma string withouth ending ","
#     """
#     hold = ""
#     numComma = ""
#     for i in range(a, b):
#         numComma = str(multiplication(i, i)) + ","
#         hold += numComma
#
#     return hold[:-1]
# https://stackoverflow.com/questions/15478127/remove-final-character-from-string-python?answertab=votes#tab-top


ANSWER = multiplicator(4, 16)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.8 (1 points)
#
# Create a function called `squares_in_range`. Inside the function create a
# loop that iterates from 4 to 15 (both included). For each number use the
# `multiplication` function from above to get the square of the current
# number. Use the `in_range` function to check if the value is between 50 and
# 100. The function should return a comma-separated string of either
# `"Inside"` or `"Outside"`,  without an ending `,`. Use an if-statement to
# concatenate the strings to the return value.
#
# Answer with a call to the function `squares_in_range`.
#
# Write your code below and put the answer into the variable ANSWER.
#
def squares_in_range():
    """
    A that sorts the squares of number between 4 and 16 into a range of
    50 <sq. of number < 100 using the in_range value above.
    It returns a comma-separated values in the range
    """
    insideRange = "Inside,"
    outsideRange = "Outside,"
    output = ""

    for num in range(4, 16):
        if in_range(multiplication(num, num)):
            output += insideRange
        else:
            output += outsideRange

    return output[:-1]

ANSWER = squares_in_range()

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.8", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.9 (1 points)
#
# Create a function called `decider`. The function takes one argument. If the
# argument is a string return a call to `funny_word()`, if the argument is an
# integer return the square of the argument by using the `multiplication`
# function.
#
# Answer with a call to the function `decider` with the argument blunderbuss.
#
# Write your code below and put the answer into the variable ANSWER.
#
def decider(arg):
    """
    A program that execute subcodes based on the argument type
    If the argument is string, funny_word() is called.
    If argument is integer, multiplicaiton() is called.
    """
    if isinstance(arg, str):
        return funny_word(arg)
    elif isinstance(arg, int):
        return multiplication(arg, arg)

ANSWER = decider("blunderbuss")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.9", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.10 (1 points)
#
# Create a function called `double_decider`. The function takes two
# arguments. For each argument call the `decider` function. Concatenate the
# returned values in a string.
#
# Separate the two values by ' and the square is '.
#
# Answer with a call to the function `double_decider` with the arguments:
# filibuster and 14.
#
# Write your code below and put the answer into the variable ANSWER.
#

def double_decider(arg1, arg2):
    """
    A function that concatenates the values of two arguments into a string
    using the decider() function above
    """
    joined = " and the square is "
    first = decider(arg1)
    second = decider(arg2)
    return first + joined + str(second)

ANSWER = double_decider("filibuster", 14)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.10", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (3 points)
#
# Create a function that returns a binary string value of a given integer.
# Return only the binary number and not any identification that it is a
# binary number.
#
# Example: Calling the function with the number 3 should return `"11"`.
#
# Answer with a call to the function with the argument 98.
#
# Write your code below and put the answer into the variable ANSWER.
#
def binaryNumber(num):
    """
    A function that calculates the binary number from any decimal number
    """
    binNum = ""

    while num > 0:
        remainder = num % 2
        binNum += str(remainder)
        num = int(num / 2)

    return binNum[::-1]

ANSWER = binaryNumber(98)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (3 points)
#
# Write a Python function that accepts a string and calculate the number of
# upper case letters and lower case letters. The function should return a
# string with the format "Lower case letters: #, upper case letters: #". Only
# count letters, you can ignore space and special characters.
#
# Answer with a call to the function with the argument: `"Pack my Box with
# five dozen LiQuor juGs."`.
#
# Write your code below and put the answer into the variable ANSWER.
#
def countUpperCase(sentence):
    """
    A function that counts upper case numbers in a text.
    @ inpara: string
    @ return: number of upper case letters in inpara
    """
    countUpper = 0
    countLower = 0
    characters = str(sentence)
    for ch in characters:
        if ch.isupper():
            countUpper += 1
        elif ch.islower():
            countLower += 1
    return "Lower case letters: {lNum}, upper case letters: {uNum}".format(lNum=countLower, uNum=countUpper)

ANSWER = countUpperCase("Pack my Box with five dozen LiQuor juGs.")

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)


dbwebb.exit_with_summary()
