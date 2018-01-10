#!/usr/bin/env python3

"""
5ebe4d25b7e0f78e815c175d4db3fc2a
python
lab2
v2
lobe16
2017-09-03 15:49:52
v2.3.3 (2017-06-12)

Generated 2017-09-03 17:49:53 by dbwebb lab-utility v2.3.3 (2017-06-12).
https://github.com/mosbth/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 2 - python
#
# In this exercise we will look into flow-control. If-statements, for-loops
# and while-loops.
#



# --------------------------------------------------------------------------
# Section 1. Boolean operators and if-statements
#
# The basics of boolean operators and if-statements.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create three variables representing dice values: `dice1` = 2, `dice2` = 6
# and `dice3` = 2.
#
# Answer with the boolean value of the expression '`dice1` is greater than
# `dice2`'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice1 = 2
dice2 = 6
dice3 = 2

ANSWER = False

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Sum the three variables `dice1`, `dice2` and `dice3`.
#
# Use an if-statement to decide if the sum of the three variables i greater
# than 11. If the sum is greater than 11 answer with 'big' otherwise answer
# with 'small'.
#
# Write your code below and put the answer into the variable ANSWER.
#

sumDices = dice1 + dice2 + dice3

checkSum = ""

if sumDices > 11:
    checkSum = "big"
else:
    checkSum = "small"

ANSWER = checkSum

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Add the sum of `dice4` = 2 and `dice5` = 1 to the sum of the three other
# dices.
#
# Use an if, elseif, else statement to check the total value of the dices.
# Answer with 'small' if the sum is smaller than 11, 'intermediate' if the
# sum is greater than or equal to 11 but smaller than 21. If the sum is
# greater than or equal to 21 answer with 'big'.
#
# Write your code below and put the answer into the variable ANSWER.
#

dice4 = 2

dice5 = 1

newSum = dice4 + dice5

sumDices += newSum

newChecks = ""

if sumDices < 11:
    newChecks = "small"
elif sumDices >= 11 or sumDices < 21:
    newChecks = "intermediate"
else:
    newChecks = "big"

ANSWER = newChecks

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Create a variable `summer_word` containing the word 'resort'.
#
# Answer with True if `summer_word` contains the letter 's' otherwise answer
# with False.
#
# Tip: Use the `in` operator.
#
# Write your code below and put the answer into the variable ANSWER.
#

summer_word = "resort"
found = False
for character in summer_word:
    if character == "s":
        found = True
        break

ANSWER = found

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. For-loops
#
# The basics of iteration and for-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Loop through the numbers 0 to 10 (10 included) and concatenate a string
# with the numbers comma-separated. You should have a comma at the end of the
# string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

commaWords = ""
for i in range(11):
    commaNumber = str(i) + ","
    commaWords += commaNumber

ANSWER = commaWords

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Loop through the letters of the variable `summer_word` from above.
# Concatenate the consonants from `summer_word` and answer with the new word.
#
# Write your code below and put the answer into the variable ANSWER.
#

vowels = "aeiou"
consonants = ""
for char in summer_word:
    if char not in vowels:
        consonants += char

ANSWER = consonants

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Loop through all numbers from 22 to 80 both numbers included. Add all odd
# (udda) numbers together and answer with the result.
#
# Tip: Use the modulus % operator.
#
# Write your code below and put the answer into the variable ANSWER.
#
sumOdds = 0
for number in range(22, 81):
    if(number % 2 > 0):
        sumOdds += number

ANSWER = sumOdds

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. While-loops
#
# The basics of while-loops.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (1 points)
#
# Create a while-loop that starts at value 4 and ends when the value is
# greater than 26, the value should be incremented by 3 for each iteration.
# Concatenate a string with the numbers comma-separated. You should have a
# comma at the end of the string.
#
# Answer with the string.
#
# Write your code below and put the answer into the variable ANSWER.
#

start = 4
stop = 26
interval = 3
stringNumber = ""

while(start <= stop):
    commaNum = str(start) + ","
    stringNumber += commaNum
    start += interval

ANSWER = stringNumber

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (1 points)
#
# Create a while-loop that adds 4 to the number 73, 26 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#

incrementBy4 = 4
addedNumber = 73
iterations = 26
count = 1

while count <= iterations: # or count < iterations if count = 0
    addedNumber += incrementBy4
    count += 1

ANSWER = addedNumber

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.3 (1 points)
#
# Create a while-loop that subtracts 5 from 40, 78 times. Answer with the
# result.
#
# Write your code below and put the answer into the variable ANSWER.
#
count = 0
subtracted = 40
subtractValue = 5
iterations = 78
while count < iterations:
    subtracted -= subtractValue
    count += 1

ANSWER = subtracted

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.3", ANSWER, False)

# --------------------------------------------------------------------------
# Section 4. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.1 (3 points)
#
# Use a for-loop or a while-loop to reverse the word 'constitutionality'.
#
# Answer with the reversed word.
#
# Write your code below and put the answer into the variable ANSWER.
#
word = "constitutionality"
reversedWord = ""
lword = len(word)-1
for char in word:
    reversedWord += word[lword]
    lword -= 1

# using while loop
# while lword >= 0:
#     reversedWord += word[lword]
#     lword -= 1

ANSWER = reversedWord

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 4.2 (3 points)
#
# Swedish numberplates consist of three letters and three numbers. The
# numbers range from 001 to 999. Using one of the four common rules of
# arithmetics (+, -, *, /), how many of the numberplates can the two first
# numbers give the third number?
#
# Examples:
# 'ABC123' can be combined to 1 + 2 = 3. So this numberplate is good.
# 'ABC129' 1 and 2 cannot be combined to give 9 using the four rules of
# arithmetics, so this does not work.
#
# Do not count multiple times if more than one rule of arithmetics work.
#
#
# Answer with the number of numberplates.
#
# Write your code below and put the answer into the variable ANSWER.
#

def isGoodCombination(num1, num2, num3):
    """
    function to check if three numbers meet a criteria for number plate
    using the three arithmetic rules of + / * -
    """
    if num1 + num2 == num3:
        return True
    elif num1 - num2 == num3:
        return True
    elif num1 * num2 == num3:
        return True
    elif num2 > 0 and (num1 / num2 == num3):
        return True



numberPlates = 0
newString = ""

for num in range(1, 1000):
    strNum = str(num)
    if num < 10:
        newString = "00" + strNum

    elif num >= 10 and num < 100:
        newString = "0" + strNum

    else:
        newString = strNum

    # print(newString)
    first = int(newString[0])
    second = int(newString[1])
    third = int(newString[2])

    if isGoodCombination(first, second, third):
        numberPlates += 1

    # if (first - second) == third:
    #     numberPlates += 1
    #
    # elif first + second == third:
    #     numberPlates += 1
    #
    # elif (second != 0) and ((first / second) == third):
    #     numberPlates += 1
    #
    # elif (first * second == third):
    #         numberPlates += 1

ANSWER = numberPlates

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("4.2", ANSWER, False)


dbwebb.exit_with_summary()
