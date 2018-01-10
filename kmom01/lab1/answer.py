#!/usr/bin/env python3

"""
f25ea6f9c1912f1a710ebcaebe907288
python
lab1
v2
lobe16
2017-09-01 11:50:48
v2.3.3 (2017-06-12)

Generated 2017-09-01 13:50:48 by dbwebb lab-utility v2.3.3 (2017-06-12).
https://github.com/mosbth/lab
"""

from dbwebb import Dbwebb

# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 1 - python
#
# If you need to peek at examples or just want to know more, take a look at
# the [Python manual](https://docs.python.org/3/library/index.html).
#
# There you will find everything this lab will go through and much more.
#



# --------------------------------------------------------------------------
# Section 1. Integers, floats and basic arithmetics
#
# The foundation of numbers and basic arithmetic.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a variable called `num_one` and give it the value 38.
#
# Answer with the value of `num_one`.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_one = 38

ANSWER = num_one

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Create another variable called `num_two` and give it the value 78. Create a
# third variable called `result` and assign to it the sum of the first two
# variables.
#
# Answer with the `result` variable.
#
# Write your code below and put the answer into the variable ANSWER.
#

num_two = 78

result = num_one + num_two

ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Create a variable called `num_three` and give it the value 70.
#
# Create another variable called `num_four` and give it the value 26.
#
# Subtract `num_three` from `num_four` and add the `result` variable from
# above to result of the subtraction. Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
num_three = 70

num_four = 26

result += (num_four - num_three)


ANSWER = result

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Answer with the result of a multiplication of `num_one` and `num_three`.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = num_one * num_three

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Create a variable called `float_one` and give it the value 31.3.
#
# Create another variable called `float_two` and give it the value 21.86.
#
# Sum the two values and answer with the result, rounded to two decimals.
#
# Write your code below and put the answer into the variable ANSWER.
#
float_one = 31.3

float_two = 21.86

ANSWER = round((float_one + float_two), 2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# All variables used in the exercise below are defined above.
#
# Sum `num_three` with `num_one` and subtract `num_four`. Multiply the result
# by `num_two`, add `float_two` and subtract `float_one`.
#
# Answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#
sum1_3 = num_three + num_one
subtr4 = sum1_3 - num_four
multiBySum2 = subtr4*num_two
addFloat2AndSubtrFloat1 = float_two - float_one
final = multiBySum2 + addFloat2AndSubtrFloat1
ANSWER = final

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Strings and concatenation
#
#
#

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Concatenate (svenska: konkatenera) the two words 'storage' and 'icecream'
# and answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

stor = "storage"

icecr = "icecream"


ANSWER = stor + icecr

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Concatenate the word 'icecream' with the integer 38 with a space between
# the two variables and answer with the result.
#
# Write your code below and put the answer into the variable ANSWER.
#

num38 = 38

space = " "

ANSWER = icecr + space + str(num38)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Concatenate the integer 38 with the word 'storage' with a space between. To
# the resulting string concatenate the string ' and '. To this string
# concatenate integer 78 and the word 'icecream' with a space between between
# the two variables.
#
# Write your code below and put the answer into the variable ANSWER.
#

num78 = 78

longStr = str(num38) + space + stor + " and " + str(num78) + space + icecr

ANSWER = longStr

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Assign the string value '30' to a variable called `string_number` and
# assign the integer value 5 to a variable called `actual_number`.
#
# Use `int()` to change the type of `string_number` to an integer and divide
# the integer value with `actual_number`. Answer with an integer by using the
# function `round()`.
#
# Write your code below and put the answer into the variable ANSWER.
#

string_number = "30"

actual_number = 5

roundDivision = round(int(string_number)/actual_number)

ANSWER = roundDivision

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Two large and one small pumps can fill a swimming pool in four hours. One
# large and three small pumps can also fill the same swimming pool in four
# hours. How many minutes will it take four large and four small pumps to
# fill the swimming pool?
#
# (We assume that all large pumps are similar and all small pumps are also
# similar.)
#
# Answer with the number of minutes.
#
# Write your code below and put the answer into the variable ANSWER.
#

"""
let
largeP = rate at which a large pump fills the pool
smallP = rate at which a small pump fills the pool

2*largeP + smallP  ==> 4 --- eq1
largeP + 3*smallP ==> 4  --- eq2

Equating eq1 = eq2 gives us that
largeP = 2*smallP --- eq3

If 2*largeP + 1*smallP fills the pool in 4 hours, this means that,

2*(2*smallP) + smallP = 5*smallP fills the pool in 4 hours.

Giving us that 1 smallP fills the pool in 4 * 5 hours.

Time to fill the pool by 4smallP and 4largeP is

4*largeP + 4*smallP = 4*(2*smallP) + 4*smallP = 12*smallP fills the pool in
4*5/12 hours

"""
fillingTime = 4 * 5 / 12


ANSWER = fillingTime * 60


# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Peter has the phonenumber '0731415926' and Anders has the phonenumber
# '0727182818'. They call each other every sunday afternoon for 9 minutes.
# Calculate the number of hours that they talk with each other pr year
# (assume 52 sundays pr year). Use that number in a string concatenation with
# the following format: 'Peter calls from [#Peter's phonenumber] to Anders on
# [#Anders's phonenumber] for [#hours] hours every year.' Replace the content
# inside [#] with the corresponding values.
#
# Answer with the concatenated string.
#
# Write your code below and put the answer into the variable ANSWER.
#
peterPhone = "0731415926"

andersPhone = "0727182818"

weeklyCalls = 9

yearWeeks = 52

yearlyMinutes = 9*yearWeeks

yearlyHours = yearlyMinutes/60

sentence = "Peter calls from " + peterPhone + " to Anders on "\
            + andersPhone +  " for " + str(yearlyHours) + " hours every year."

ANSWER = sentence

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, True)


dbwebb.exit_with_summary()
