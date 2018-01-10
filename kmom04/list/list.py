#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bernard Longho, 2017-09-24
Wetting my hands on lists.
Examples from: https://dbwebb.se/kunskap/kom-igang-med-datatypen-lista-i-python
"""
# create an empty list and start working from There
shopping = []

shopping = ["köttfärs", "krossade tomater", "gräde", "gul lök"]

shopping.insert(0, "grädde")

print(shopping)

remove = shopping.pop(4)

print(remove)
print(shopping)

# Show items in the shopping list with a number
for i, item in enumerate(shopping):
    print("{}. {}".format(i+1, item))
