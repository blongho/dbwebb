#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bernard Che Longho, 2017-10-01
Working with dictionaries.
Reading and applying exercises from
https://www.py4e.com/html3/09-dictionaries
"""
import string
"""
eng2sp = dict()
print(eng2sp)

eng2sp["one"] = "uno"

#print(eng2sp)

eng2sp = {"one": "uno", "two": "dos", "three": "trees"}
print(eng2sp)

# print(eng2sp["uno"]) # error since this is a mapping value of key "one"

# Get number of keypairs
#print("Number of key pairs:", len(eng2sp))

# values() makes the dictionary into a list
val = list(eng2sp.values()) # returns the values (NOT the keys!)
#print(val)

word = "brontosaurus"

d = dict()
# print(d)
# for c in word:
#     if c not in d:
#         d[c] = 1
#     else:
#         d[c] += 1
# print(d)

for c in word:
    d[c] = d.get(c, 0) + 1
print(d)

# Number of "r" in the dictionar
print(d.get("r", 0))
"""

"""
Dictionaries and files
"""
fname = "romeo.txt"
try:
    with open(fname) as fil:
        content = fil.read().splitlines()
except IOError:
    print("Error reading file '{fn}'".format(fn=fname))
    exit()

# print(content)

counts = dict()

for line in content:
    words = line.split()
    for word in words:
        if word not in counts:
            counts[word] = 1
        else:
            counts[word] += 1
# print(counts)
# try:
#     fhand = open(fname)
# except IOError:
#     print("File cannot be opened:", fname)
#     exit()
#
#
# for line in fhand:
#     words = line.split()
#     for word in words:
#         if word not in counts:t
#             counts[word] = 1
#         else:
#             counts[word] += 1
# print(counts)

# for key in counts:
#     print(key, counts[key])

"""
Printing a dictionary in a sorted mannar
"""
lst = list(counts.keys())
# print(lst) # prints the keys(words)

# sort the keys(words)
lst.sort()
for key in lst:
    print(key, counts[key])

"""
Advanced text parsing
"""
# Working with a more complicated version of remeo.txt
"""
But, soft! what light through yonder window breaks?
It is the east, and Juliet is the sun.
Arise, fair sun, and kill the envious moon,
Who is already sick and pale with grief,
"""

filename = "romeo_punc.txt"

try:
    filhand = open(filename)
except IOError:
    print("File cannot be opend:", filhand)
    exit()

counts2 = dict()
for line in filhand:
    line = line.rstrip()
    line = line.translate(line.maketrans('', '', string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        if word not in counts2:
            counts2[word] = 1
        else:
            counts2[word] += 1
print(counts2)
