#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
2017-10-01
Bernard Longho
Exercise 1:
[wordlist2] from
https://www.py4e.com/html3/09-dictionaries

Write a program that reads the words in words.txt and stores them as
keys in a dictionary. It doesn't matter what the values are. Then you can
use the in operator as a fast way to check whether a string is in thedictionary.
"""
fname = "words.txt" # from

# http://www.py4inf.com/code/words.txt

# read all content of the file
file_content = ""
try:
    with open(fname) as fil:
        file_content = fil.read().splitlines()
except IOError:
    print("Error opening file with filename {fn}".format(fn=fname))
    exit()

#print(file_content)

# create dictionary to hold the words
word_dict = dict()

# for each line in file, split content, save each word as key in dictionary
for line in file_content:
    line_as_list = line.split()
    for word in line_as_list:
        if word not in word_dict:
            word_dict[word] = 1
        else:
            word_dict[word] = word_dict[word] + 1

# How many times does the word "you" appear in this dictionary
print("The string '{you}' appears in 'words.txt' {n} times.".format(
    you="you", n=word_dict["you"]))

# This could still be achieved using the get method
print("{you}' appears in the dictionary is {times}".format(you="you", times=word_dict.get("you", 0)))
