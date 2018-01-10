#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bernard Longho, 2017-09-24
Attempting exercises 7.11 in python for informatics
"""
# Reading files

# ==============================================================================
"""
Exercise 1: Write a program to read through a file and print the contents of the
file (line by line) all in upper case.
Executing the program will look as follows:

python shout.py
Enter a file name: mbox-short.txt
FROM STEPHEN.MARQUARD@UCT.AC.ZA SAT JAN 5 09:14:16 2008
....
"""
def openFile():
    """
    Returns a file handler that has successfully opened a file
    """
    file_name = input("Enter the file name: ")
    try:
        fhand = open(file_name)
    except IOError:
        print(file_name, "could not be opened.")
        exit()
    return fhand
# ============================================================================
def openFunnyFile():
    """
    Returns a file handler that has successfully opened a file or a runny string
    NA NA BOO BOO TO YOU - You have been punk'd! if person enters
    "na na boo boo"
    """
    funnyName = "na na boo boo"
    file_name = input("Enter the file name: ")
    if file_name == funnyName:
        print(funnyName.upper(), "TO YOU - You have been punk'd")
        exit()
    try:
        fhand = open(file_name)
    except IOError:
        print(file_name, "could not be opened.")
        exit()
    return fhand

# =============================================================================
# 7.1
# fhand = openFile()
#
# for line in fhand:
#     line = line.rstrip()
#     print(line.upper())

# ==============================================================================
"""
Exercise 2: Write a program to prompt for a file name, and then read through the
file and look for lines of the form:
When you encounter a line that starts with “X-DSPAM-Confidence:” pull apart
the line to extract the floating-point number on the line. Count these lines and
then compute the total of the spam confidence values from these lines. When you
reach the end of the file, print out the average spam confidence.

Enter the file name: mbox.txt
Average spam confidence: 0.894128046745
Enter the file name: mbox-short.txt
Average spam confidence: 0.750718518519
"""
# 7.2
file_handler = openFile()
search_string = "X-DSPAM-Confidence:"
count_spam = 0
sum_spam_conf = 0

for line in file_handler:
    if line.startswith(search_string):
        count_spam += 1
        colPos = line.find(":")
        spam_conf = line[colPos+1:]
        sum_spam_conf += float(spam_conf.rstrip())
print("Average of spam confidence is %F" %(sum_spam_conf/count_spam))

# ============================================================================
# 7.3
subj = "Subject:"
f_hand = openFunnyFile()

count_subj_lines = 0
for line in f_hand:
    if line.startswith(subj):
        count_subj_lines += 1
print("There are %d subject lines in this file" %count_subj_lines)
