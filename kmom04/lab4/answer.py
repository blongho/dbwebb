#!/usr/bin/env python3

"""
cfc632ef66b7b06150623ec718de8562
python
lab4
v2
lobe16
2017-09-24 15:08:11
v2.3.3 (2017-06-12)

Generated 2017-09-24 17:08:12 by dbwebb lab-utility v2.3.3 (2017-06-12).
https://github.com/mosbth/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 4 - python
#
# "In these exercises we will take a look into lists."
#



# --------------------------------------------------------------------------
# Section 1. List basics
#
#
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Concatenate the two lists [flute, Sheen] and [wall, bumblebee].
#
# Answer with your list.
#
# Write your code below and put the answer into the variable ANSWER.
#
list1 = ["flute", "Sheen"]
list2 = ["wall", "bumblebee"]

ANSWER = list1 + list2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# Use the list [lion, tiger, ozelot, bobcat, cougar].
#
# Add the words 'hotdog' and 'donkey' as the second and third element.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#
animal_list = ["lion", "tiger", "ozelot", "bobcat", "cougar"]

mixed_list = animal_list[:]

mixed_list.insert(1, "hotdog")
mixed_list.insert(2, "donkey")


ANSWER = mixed_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the list [lion, tiger, ozelot, bobcat, cougar].
#
# Replace the third word with: 'cord'.
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

replaced_list = animal_list[:]
replaced_list[2] = "cord"

ANSWER = replaced_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Sort the list
#
# > [lion, tiger, ozelot, bobcat, cougar]
#
# in descending alphabetical order. Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

rsorted_animal_list = animal_list[:]

rsorted_animal_list.sort(key=None, reverse=True)

ANSWER = rsorted_animal_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Use `remove()` to delete the word:
#
# > 'wall'
#
# from the list:
#
# > [table, wall, desk, chair, floor]
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

list_to_remove = ["table", "wall", "desk", "chair", "floor"]

list_to_remove.remove("wall")

ANSWER = list_to_remove

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Built-in list functions
#
# Some basic built-in functions.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Use a built-in function to sum all numbers in the list:
#
# > [67, 50, 2, 39, 15]
#
# Answer with the result as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

int_list = [67, 50, 2, 39, 15]

ANSWER = sum(int_list)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Use built-in functions, such as `sum` and `len` to get the average value of
# the list:
#
# > [567, 23, 12, 36, 7]
#
# Answer with the result as a float with at most one decimal.
#
# Write your code below and put the answer into the variable ANSWER.
#

int_list2 = [567, 23, 12, 36, 7]

ANSWER = sum(int_list2)/len(int_list2)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the built-in functions `split()` and `join()` to fix this string:
#
# > "The?sun?is?shining"
#
# into a real sentence, (without '?').
#
# Answer with the fixed string.
#
# Write your code below and put the answer into the variable ANSWER.
#
error_string = "The?sun?is?shining"

#print(error_string)

split_str = error_string.split("?")

#print(split_str)

fixed_string = " ".join(split_str)

#print(fixed_string)
ANSWER = fixed_string
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Use slice on the list
#
# > [a, b, c, d, e]
#
# and replace the second and third element with
#
# > "freezer, fridge"
#
# Answer with the modified list.
#
# Write your code below and put the answer into the variable ANSWER.
#

char_list = ["a", "b", "c", "d", "e"]

char_list[1] = "freezer"

char_list[2] = "fridge"

ANSWER = char_list

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.5 (1 points)
#
# Assign the list
#
# > [b, a, e, d, c]
#
# to a variable called 'list1'.
#
# Assign the list again, but to another variable called 'list2'.
#
# Answer with the result of 'list1 is list2'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list_1 = ["b", "a", "e", "d", "c"]

list_2 = ["b", "a", "e", "d", "c"]

ANSWER = list_1 is list_2

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.6 (1 points)
#
# Use your lists from the last exercise. Assign 'list1' to another variable
# called 'list3' like this:
#
# > list3 = list1
#
# Answer with the result of 'list1 is list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list_3 = list_1

ANSWER = list_1 is list_3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.7 (1 points)
#
# Use your lists from the last exercise. Change the first element in 'list1'
# to
#
# > "y"
#
# Answer with 'list3'.
#
# Write your code below and put the answer into the variable ANSWER.
#

list_1[0] = "y"

ANSWER = list_3

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 3. Extra assignments
#
# These questions are worth 3 points each. Solve them for extra points.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.1 (3 points)
#
# Create a function that returns the list passed as argument sorted in
# numerical and ascending order. Also multiply all values with 10.
#
# Use the list:
#
# > [45, 22, 2, 498, 78]
#
# and the built-in method `sort()`.
#
# Answer with the sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#
def multiply_and_sort_list(a_list, multiple):
    """
    Multiplies all the numbers in a list by 10 and returns the list sorted in
    ascending order
    """
    new_list = []
    for num in a_list:
        new_list.append(num * multiple)

    new_list.sort()
    return new_list

num_list = [45, 22, 2, 498, 78]

ANSWER = multiply_and_sort_list(num_list, 10)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Create a function that takes the list:
#
# > [567, 23, 12, 36, 7]
#
# as argument.
#
# The function should multiply all even numbers by 2 and add 5 to all odd
# numbers.
#
# Answer with the modified list sorted in numerical order, descending.
#
# Write your code below and put the answer into the variable ANSWER.
#

def manipulate_num_list(a_list, mult_factor, add_factor):
    """
    Takes a list, multiply even numbers by 2 and adds 5 to odd numbers.
    Returns the list sorted in descending order.
    """
    new_list = []
    for num in a_list:
        if num % 2 == 0:
            new_list.append(num * mult_factor)
        if num % 2 != 0:
            new_list.append(num + add_factor)

    new_list.sort(key=None, reverse=True)
    return new_list


n_list = [567, 23, 12, 36, 7]

mult_fact = 2

add_fact = 5


ANSWER = manipulate_num_list(n_list, mult_fact, add_fact)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
