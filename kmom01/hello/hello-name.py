#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Some various ways of saying Hello World in Python.
"""

# Print out Hello World
print("Just saying Hello World")

# Assign the string Hello World to a variable and print it out
str1 = "Hello World in a variable"
print(str1)

# Combine two strings and print them out
str2 = "Hello World!"
str3 = "Its a nice day today!"
print(str2 + " " + str3)

# Combine string and values
a = 40
b = 2
c = a + b
str4 = "Summan är " + str(c) + "."
print(str2 + " " + str4)

# Print out my name
name = "Bernard Che Longho"
print("Mitt namn är " + name)

# Print out ASCII art
# Use prefix r for a raw string avoiding validation
marvin = r"""
Jag tycker mycket om bilar, särskild stora bilar. Denna är den jag
köper om xx år
                                       ________________________
                        ,---------+/       +----------+     \
                      /          ||        |          |      |
                    /            ||        +----------+      |
   _________------=--<I|---------+----------------------------,
 .----=============|=========---=|=======================-->> |
 |     ______      |             |              ______        |
[|    / _--_ \     /             |         / _--_ \       ]
  \__|| -__- ||___/_____________/_____________|| -__- ||_____/
       \____/                                   \____/

"""
print(marvin)

marvin1 = r"""
                           (_)
              __        __        __        __
 .*.        /~ .~\    /~  ~\    /~ .~\    /~  ~\
 ***       '      `\/'      *  '      `\/'      *
  V       (                .*)(               . *)
/\|/\      \    Bernard . *./  \      Honorine  . *./
  |         `\ .      . .*/'    `\ .      . .*/'       .*.
  |           `\ * .*. */' _    _ `\ * .*. */'         ***
                `\ * */'  ( `\/'*)  `\ * */'          /\V
                  `\/'     \   */'    `\/'              |/\
                            `\/'                        |
                            LOVES
========================================================================
"""
print(marvin1)
