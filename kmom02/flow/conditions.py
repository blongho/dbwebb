#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bernard Longho
2017-09-03
Working with conditions in python3
from https://dbwebb.se/kunskap/villkor-och-loopar
"""
# if-else statement
numOfApples = 9

if numOfApples > 10:
    print("Du har mer än 10 äpplen")
elif numOfApples <= 10 and numOfApples > 5:
    print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
else:
    print("Du har nog varit hungrig och ätit upp dina äpplen")

# nested if - else

typeOfFruit = input("Enter the name of a fruit: ")

# Ask for integer till valid interger is entered
while True:
    try:
        numOfFruits = int(input("How many fruits : "))
    except ValueError:
        print("I expected an integer for the number of fruits.")
        continue
    else:
        break
        # good number gotten, so we go futher

# process rest of block here
if numOfFruits > 10:
    if typeOfFruit == "äpple":
        print("Du har mer än 10 äpplen")
    else:
        print("Du har mer än 10 frukter")
