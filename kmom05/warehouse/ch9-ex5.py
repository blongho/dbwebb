#!/usr/bin/env python3
# -*- coding: utf-8 -*

"""
Bernard Longho
2017-10-03
Working on exercise 5
https://www.py4e.com/html3/09-dictionaries#exercises
"""

"""
Exercise 5:
This program records the domain name (instead of the address) where the message
was sent from instead of who the mail came from (i.e., the whole email
address). At the end of the program, print out the contents of your dictionary.

python schoolcount.py
Enter a file name: mbox-short.txt
{'media.berkeley.edu': 4, 'uct.ac.za': 6, 'umich.edu': 7,
'gmail.com': 1, 'caret.cam.ac.uk': 1, 'iupui.edu': 8}

"""

fname = input("Enter file name: ")

content = ""
try:
    with open(fname) as mail:
        content = mail.read().splitlines()
except IOError:
    print("Error reading '{fn}'".format(fn=fname))
    exit()

domain_dict = dict()
for line in content:
    if line.startswith("From "):
        words = line.split()
        email = words[1].rstrip()
        domain = email.split("@")[1]
        # splits 2nd item in words at @, take 2 part
        domain_dict[domain] = domain_dict.get(domain, 0) + 1

for domain in domain_dict:
    print(str(domain).ljust(18), str(domain_dict[domain]).rjust(5))
