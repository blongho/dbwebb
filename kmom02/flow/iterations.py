#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bernard Longho
2017-09-03
Working with iterations in python3
from https://dbwebb.se/kunskap/villkor-och-loopar
"""

# Working with loops now

# The for loop in python3
print("\nPrinting number from 0 to 10 in a vertical manner")
for i in range(10): # 0 to n-1
    print(i) # prints number from 0 to 9

# print the numbers horizontally
print("\nPrinting numbers from 0 to 10 horizontally")
for i in range(10):
    print(i, end=" ")

# print in defined range
start = 3
stop = 15
print("\nPrinting numbers between", str(start), "and", str(stop))
for i in range(start, stop):
    print(i, end=" ") # prints 3 4 5 ... 14


# Using interval in range
interval = 2
print("\nPrinting numbers with specific interval incrementation, heree 2")
for i in range(start, stop, interval):
    print(i, end=" ") # prints 3 5 ... 13

# Use for to search and count occurence
count = 0
print("\n")
word = "räksmörgås"
for letter in word:
    if letter in "åäö":
        count += 1
        print(letter)
print("There were", str(count), "swedish characters in", word)

# while loop with except
while True:
    user_input = input("Skriv in antal äpplen (eller q för avslut): ")
    # check if user wants to run the program or not
    if user_input == "q":
        print("Du är nu klar med att äta äpplen.")
        print("Hej då!")
        break
    else: # a value is entered, convert to int, then check
        try:
            number_of_apples = int(user_input)
        except ValueError:
            print("Oj! Du skrev inte in en siffra.")
            continue

        if number_of_apples > 10:
            print("Du har mer än 10 äpplen")
        elif number_of_apples <= 10 and number_of_apples > 5:
            print("Du blev snabbt mätt och åt bara upp några av dina äpplen")
        else:
            print("Du har nog varit hungrig och ätit upp dina äpplen")
