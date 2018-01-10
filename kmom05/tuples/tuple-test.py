#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
Bernard Longho
2017-10-03
Working on tuples
https://www.py4e.com/html3/10-tuples
"""
import string
"""
# Comparing tuples
t1 = (0, 1, 2)
t2 = (0, 3, 4)
answer = "Yes" if t1 > t2 else "No"
print("Is {t1} > {t2}? {ans}".format(t1=t1, t2=t2, ans=answer))

"""

"""
# Demonstrating DSU
txt = "but soft what light in yonder window breaks"

words = txt.split()

t = list()
for word in words:
    t.append((len(word), word))

t.sort(reverse=True)

print(t)

res = list()
for length, word in t:
    res.append(word)

print(res)
"""

"""
# Demonstrating some weird kinds of assignment
m = ["have", "fun"]

x, y = m

print(x)
print(y)
a, b = 3, 4

print(b)
email = "line01@student.bth.se"

# extract user name and domain
uname, domain = email.split("@")
print("User name: {un}\nDomain: {dm}".format(un=uname, dm=domain))
"""

"""
# Dicitionaries and tuples

d = {"a": 10, "c": 22, "b": 1}
t = list(d.items())
print(t)
t.sort()
print(t)

for key, val in list(d.items()):
    print(str(val).ljust(3), str(key).rjust(2))
"""

"""
# The most common words in http://www.py4inf.com/code/romeo-full.txt
"""
fhand = open("romeo-fulltext.txt")
counts = dict()
for line in fhand:
    line = line.translate(str.maketrans("", "", string.punctuation))
    line = line.lower()
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1

# Sort the dictionary by value
lst = list()
for key, val in list(counts.items()):
    lst.append((val, key))

lst.sort(reverse=True)

for key, val in lst[:20]: # slices the list from beginning to 10th element
    print(key, val)
