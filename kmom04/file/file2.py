#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bernard Longho, 2017-09-24
Wetting my hands on files.
Examples from: https://dbwebb.se/kunskap/att-lasa-filer-i-python#lasa
"""
fileName = "items.txt"

# with - as for reading a file automatically closes it after reading is done
with open(fileName) as itemsFile:
    line = itemsFile.readline().strip() # strip removes whitespace, tab, newline
print(line)

# Split lines into list of the comma

items_as_list = line.split(",")

print(items_as_list)

items_as_list.append("cup")

print(items_as_list)

# Join the list with comma between every items_as_list

list_as_str = ",".join(items_as_list)

print(list_as_str)

# write line to the file

with open(fileName, "w") as openItems:
    openItems.write(list_as_str)

print(list_as_str)
