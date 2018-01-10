#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
Bernard Longho
2017-10-03
Working on exercise 2
https://www.py4e.com/html3/09-dictionaries#exercises
"""

"""
Exercise 2:
Write a program that categorizes each mail message by which day of the week the
commit was done. To do this look for lines that start with "From", then look
for the third word and keep a running count of each of the days of the week.
At the end of the program print out the contents of your dictionary
(order does not matter).

Sample Line:

    From stephen.marquard@uct.ac.za Sat Jan  5 09:14:16 2008
Sample Execution:

python dow.py
Enter a file name: mbox-short.txt
{'Fri': 20, 'Thu': 6, 'Sat': 1}
"""
fname = input("Enter file name: ")

content = ""
try:
    with open(fname) as mail:
        content = mail.read().splitlines()
except IOError:
    print("Error reading '{fn}'".format(fn=fname))
    exit()

date_dict = dict()
for line in content:
    if line.startswith("From "):
        line_list = line.split()
        date_dict[line_list[2]] = date_dict.get(line_list[2], 0) + 1

print(date_dict)
