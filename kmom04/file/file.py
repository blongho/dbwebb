#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bernard Longho, 2017-09-24
Wetting my hands on files.
Following examples from the book "Python for informatics"
"""
# Reading files
shortFile = "mbox-short.txt"
normalFile = "mbox.txt"
#fhand = open("mbox.txt")
#shortf = open("mbox-short.txt")
# mbox contains the mail file from https://www.py4e.com/code3/mbox.txt

# counting the lines in the file
# count = 0
# for line in fhand:
#     count += 1
#     #print(line)
# print("Line count in main file:", count)

# countShort = 0
# for line in shortf:
#     countShort += 1
#
# print("Lines in the short file:", countShort)

# inp = shortf.read()    # Use this only when file is small, else use loop
# print(len(inp))
#
# print(inp[:20]) # prints out the first 20 characters of inp


# Searching through file
# Reading the file and printing lines that start with "From:"
# countShort = 0
# for line in shortf:
#     line = line.rstrip() # strips whitespace from the right side of a string
#     if line.startswith("From:"):
#         print(line)
#         countShort += 1
# print("{num} of lines starting with 'From:'.".format(num=countShort))

# making the above program from lines 35 to 39 more effective by skipping unintersting lines
# for line in shortf:
#     line = line.rstrip()
#     if not line.startswith("From:"):
#         continue
#     print(line)

# we use find() to find the first occurence of a starting
# searching for lines that contatin "@uct.ac.za"
# for line in shortf:
#     line = line.rstrip()
#     if line.find("@uct.ac.za") == -1: continue
#     print(line)

# Using try, except and open with files
# fname = input("Enter the file name: ")
# try:
#     fhand = open(fname)
# except:
#     print(fname, "cannot be opened.")
#     exit()
# count = 0
# for line in fhand:
#     if line.startswith("Subject:"):
#         count += 1
# print("There were", count, "subject lines in", fname)

# str1 = "Bernard Che Longho"
# print(repr(str1))
# # Writing files
#
# fileOut = open(shortFile, "w")
# print(fileOut)
# fileOut.write("This is a new line into the file,\n")
# fileOut.close()
