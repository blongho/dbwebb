#!/usr/bin/env python3

"""
a5e6fd567638901f3667e7c4e5a53978
python
lab5
v2
lobe16
2017-10-04 19:44:30
v2.3.3 (2017-06-12)

Generated 2017-10-04 21:44:30 by dbwebb lab-utility v2.3.3 (2017-06-12).
https://github.com/mosbth/lab
"""

from dbwebb import Dbwebb


# pylint: disable=invalid-name

dbwebb = Dbwebb()
dbwebb.ready_to_begin()



# ==========================================================================
# Lab 5 - python
#
# A look into dictionaries and tuples.
#



# --------------------------------------------------------------------------
# Section 1. Dictionaries
#
# Some basics with dictionaries.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.1 (1 points)
#
# Create a small phonebook using a dictionary. Use the names as keys and
# numbers as values.
#
# Use
#
# > Baggins, Aragorn, Smaug
#
# and corresponding numbers
#
# > 55523412, 55564222, 55567894
#
# Add the phonenumbers as integers. Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#
phonebook = {
    "Baggins" : 55523412,
    "Aragorn" : 55564222,
    "Smaug" : 55567894
}

ANSWER = phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.2 (1 points)
#
# How many items are there in the dictionary?
#
# Write your code below and put the answer into the variable ANSWER.
#

phonebook_items = len(phonebook)

ANSWER = len(phonebook)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.3 (1 points)
#
# Use the `get()` method on your phonebook and answer with the phonenumber of
# 'Baggins'.
#
# Write your code below and put the answer into the variable ANSWER.
#

baggins_phone = phonebook.get("Baggins")

ANSWER = baggins_phone

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.4 (1 points)
#
# Get all keys from the dictionary and return them in a sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#

phonebook_keys = list(phonebook.keys())

phonebook_keys.sort()

ANSWER = phonebook_keys

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.4", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.5 (1 points)
#
# Get all values from the dictionary and return them in a sorted list.
#
# Write your code below and put the answer into the variable ANSWER.
#
phonebook_values = list(phonebook.values())

phonebook_values.sort()

ANSWER = phonebook_values

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.5", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.6 (1 points)
#
# Use the in-operator to test if the name 'Baggins' exists in the dictionary.
# Answer with the return boolean value.
#
# Write your code below and put the answer into the variable ANSWER.
#

ANSWER = "Baggins" in phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.6", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 1.7 (1 points)
#
# Get and remove the item 'Baggins' from the phonebook (use pop()). Answer
# with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#

phonebook.pop("Baggins")

ANSWER = phonebook

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("1.7", ANSWER, False)

# --------------------------------------------------------------------------
# Section 2. Tuples
#
# Some basics with tuples.
#



# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.1 (1 points)
#
# Create a tuple with 'bear, 65, 6.47, chair, 5'. Answer with the length of
# the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#
mixed_tupple = ("bear", 65, 6.47, "chair", 5)

ANSWER = len(mixed_tupple)

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.2 (1 points)
#
# Create a tuple out of:
#
# > (bear, 65, 6.47, chair, 5).
#
# Assign each value in the tuple to different variables:
#
# > 'a','b','c','d','e'.
#
# Answer with the variable: 'd'.
#
# Write your code below and put the answer into the variable ANSWER.
#
#('a', 'b', 'c', 'd', 'e') = mixed_tupple

d = mixed_tupple[3]
ANSWER = d
# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.2", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.3 (1 points)
#
# Use the list
#
# > [67, 50, 2, 39, 15]
#
# Assign the first two elements to a tuple with a slice on the list.
#
# Answer with the first element in the tuple as an integer.
#
# Write your code below and put the answer into the variable ANSWER.
#

nlist = [67, 50, 2, 39, 15]

ntuple = tuple(nlist[:2])

first_in_ntuple = ntuple[0]

ANSWER = first_in_ntuple

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("2.3", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 2.4 (1 points)
#
# Create a tuple with
#
# > (moose, 12, 1.98, table, 7)
#
# Convert it to a list and replace the second element with:
#
# > "elevator"
#
# Convert it back to a tuple and answer with the first three elements in a
# comma-separated string,  without an ending `,`.
#
# Write your code below and put the answer into the variable ANSWER.
#
tup = ("moose", 12, 1.98, "table", 7)

# convert tupple to list
tup_list = list(tup)

# replace second element in list by "elevator"
tup_list[1] = "elevator"

# convert tup_list to tuple
new_tup = tuple(tup_list)

# Make a string containing the first three items in the new tuple
tup_str = ""
for itm in new_tup[:3]:
    tup_str += str(itm) + ","


ANSWER = tup_str[:-1]

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
# Use a for-loop to walk through the dictionary and create a string
# representing it. Each name and number should be on its own row, separated
# by a space. The names must come in alphabetical order. Note that every row
# should end with a newline character, `\n`.
#
# Answer with the resulting string.
#
# Write your code below and put the answer into the variable ANSWER.
#
phonebook_str = ""

phonebook_ori = {
    "Baggins" : 55523412,
    "Aragorn" : 55564222,
    "Smaug" : 55567894
}
for name in sorted(phonebook_ori.keys()):
    tmp = name + " " + str(phonebook_ori[name]) + "\n"
    phonebook_str += tmp

ANSWER = phonebook_str

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.1", ANSWER, False)

# """"""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""""
# Exercise 3.2 (3 points)
#
# Convert the phonenumber to a string and add the prefix '+1-', representing
# the language code, to each phone-number. [country code]
#
# Answer with the resulting dictionary.
#
# Write your code below and put the answer into the variable ANSWER.
#
for name in phonebook_ori:
    phonebook_ori[name] = "+1-" + str(phonebook_ori[name])

ANSWER = phonebook_ori

# I will now test your answer - change false to true to get a hint.
dbwebb.assert_equal("3.2", ANSWER, False)


dbwebb.exit_with_summary()
