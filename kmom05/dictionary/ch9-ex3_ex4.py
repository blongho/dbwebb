#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
Bernard Longho
2017-10-03
Working on exercise 3
https://www.py4e.com/html3/09-dictionaries#exercises
"""

"""
Exercise 3:
Write a program to read through a mail log, build a histogram using a
dictionary to count how many messages have come from each email address, and
print the dictionary.

Enter file name: mbox-short.txt
{'gopal.ramasammycook@gmail.com': 1, 'louis@media.berkeley.edu': 3,
'cwen@iupui.edu': 5, 'antranig@caret.cam.ac.uk': 1,
'rjlowe@iupui.edu': 2, 'gsilver@umich.edu': 3,
'david.horwitz@uct.ac.za': 4, 'wagnermr@iupui.edu': 1,
'zqian@umich.edu': 4, 'stephen.marquard@uct.ac.za': 2,
'ray@media.berkeley.edu': 1}
"""

fname = input("Enter file name: ")

content = ""
try:
    with open(fname) as mail:
        content = mail.read().splitlines()
except IOError:
    print("Error reading '{fn}'".format(fn=fname))
    exit()

email_dict = dict()
for line in content:
    if line.startswith("From "):
        words = line.split()
        for word in words:
            if "@" in word:
                email_dict[word] = email_dict.get(word, 0) + 1

print(email_dict)
# emails = list(email_dict.keys())
# emails.sort()
# for email in emails:
#     print(email, "===>", email_dict[email])

"""
Exercise 4:
Add code to the above program to figure out who has the most messages in the
file.

After all the data has been read and the dictionary has been created, look
through the dictionary using a maximum loop (see Section [maximumloop]) to find
who has the most messages and print how many messages the person has.

Enter a file name: mbox-short.txt
cwen@iupui.edu 5

Enter a file name: mbox.txt
zqian@umich.edu 195
"""
highest = max(email_dict, key=email_dict.get)

print(highest, ":", email_dict[highest])
"""
Another solution from
https://github.com/epequeno/python-for-informatics/blob/master/ch09/03.py

file_name = 'mbox-short.txt'
lines = [line.strip() for line in open(file_name, 'r')
         if line.startswith("From ")]
who_from_dict = {}

for line in lines:
    words = line.split()
    who_from_dict[words[1]] = who_from_dict.get(words[1], 0) + 1

print(who_from_dict)
"""
