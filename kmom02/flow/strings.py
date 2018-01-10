#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Working with strings
"""
# fruit = "banana"
# letter = fruit[0]
# print(letter)  # gets the first character in the string
#
# # String length
#
# length = len(fruit)
# print(length)
#
# # print last characters
#
# print("The last character of '%s' is '%s'" %(fruit, fruit[length-1]))
#
# # print string in reverse order
# print("\nPrinting the characters in the string in reverse order")
# while length > 0:
#     letter = fruit[length-1]
#     print(str(length-1), letter)
#     length -= 1
#
# # print string using for loop
# print("\nPrinting the characters in '%s'" %fruit)
# for char in fruit:
#     print(char)


# string slices --> a segment of a string

myName = "Bernard Che Longho"
#print(myName[0:5]) # prints from the first character to the 5th Berna is printed

print(myName[6:12])  # splits and prints from the 6th to the 12th character

print(myName[:3])   # prints the first three characters

print(myName[3:])   # prints from the 3rd (after it) to the end of the string

print(myName)

print(myName.upper())

print(myName.find("s")) # returns the position of the first occurence else -1

spacedString = "  We are here  "
print("Original string is '%s'" %spacedString)

# Remove white spaces at the beginning of the string
print("Formatted string is '%s'" %spacedString.strip())


print(myName.lower()) # converts everything to lower case

print(myName.capitalize())  # capitalizes the first character
