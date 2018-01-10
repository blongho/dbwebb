#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
lobe16
2017-09-01
A program to take in value and greet someone
"""
print("Hej Jack Black, du är 48 år gammal.")

current_year = 2017
name = input("Skriv ett namn, klicka sen enter : ")
age = input("Skriv en ålder, klicka sen enter : ")

year_born = str(current_year - int(age))
greeting = "Hej " + name + ", du är " + str(age) + " år gammal och föddes år " + year_born
print(greeting)
