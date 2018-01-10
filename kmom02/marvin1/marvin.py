#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import random
import math


def getInteger(someString):
    """
    a function that takes and validates an integer
    The function takes a string that tells the user what to enter and returns
    an integer
    """
    while True:
        try:
            value = int(input("\tEnter the value for %s: " %someString))
        except ValueError:
            print("\tPlease enter a valid number")
        else:
            return value

def getFloate(someString):
    """
    a function that takes and validates a float
    The function takes a string that tells the user what to enter and returns
    an integer
    """
    while True:
        try:
            value = float(input("\tEnter the value for %s: " %someString))
        except ValueError:
            print("\tPlease enter a valid number")
        else:
            return value


marvin_image = r"""
                     _______
               _/       \_
              / |       | \
             /  |__   __|  \
            |__/((o| |o))\__|
            |      | |      |
            |\     |_|     /|
            | \           / |
             \| /  ___  \ |/
              \ | / _ \ | /
               \_________/
                _|_____|_
           ____|_________|____
          /                   \  -- Marvin the genius.
"""

"""
Its an eternal loop, until q is pressed.
It should check the choice done by the user and call a appropriate
function.
"""
while True:
    print(chr(27) + "[2J" + chr(27) + "[;H")
    print(marvin_image)
    print("\tHi, I'm Marvin. I know it all. What can I do you for?")
    print("\n\tPick a number from the menu.")
    print("\t" + 40 * '-')
    print("\t1)  Present yourself to Marvin.")
    print("\t2)  How long you have lived on earth.")
    print("\t3)  Show a weight equivalent on the moon.")
    print("\t4)  Time converter.")
    print("\t5)  Celcius to fahrenhet converter.")
    print("\t6)  Word multiplication.")
    print("\t7)  Random number generator.")
    print("\t8)  Sum and average of numbers.")
    print("\t9)  Calculate the area of a circle.")
    print("\t10) Calculate hypotenus of a right-angled triangle.")
    print("\t11) Number comparisom game.")
    print("\tQ)  Quit.")
    print("\t" + 40 * '-')
    choice = input("\n\tYour choice-->: ")

    if choice == "q" or choice == "Q":
        print("\tBye, bye - and welcome back anytime!")
        break

    elif choice == "1":
        name = None
        while name is None:
            name = input("\tWhat is your name? : ")

        print("\n\tMarvin says:\n")
        print("\tHello %s - your awesomeness!" % name)

    elif choice == "2":
        age = 0
        while age < 1:
            age = getInteger("age")
            if age > 0:
                oneYear = 365*24*60*60
                stayOnEarth = age*oneYear
                print("\tWao! you have been on earth for at least %d seconds" %stayOnEarth)
                break
            else:
                print("\tAge must be greater than 0")

    elif choice == "3":
        print("\tMarvin can convert any weight to its equivalent in the moon.\n")

        earthWeight = 0
        while earthWeight < 1:
            earthWeight = getInteger("weight[kg]")
            if earthWeight > 0:
        # from http://www.learningaboutelectronics.com/Articles/Weight-on-the-moon-conversion-calculator.php#answer
                moonWeight = float((earthWeight / 9.81) * 1.622)
                print("\tThe weight of %d kg on earth is equivalent to"\
                    %earthWeight, round(moonWeight, 2), "kg on the moon.\n")
                break
            else:
                print("\tWeight must be greater than 0!")

    elif choice == "4":
        print("\tMarvin converts total minutes into hours and minutes\n")
        totalMins = 0
        while totalMins < 1:
            totalMins = getInteger("total minutes")
            if totalMins >= 1:
                hours = totalMins / 60
                mins = totalMins % 60
                print("\t%d minutes is equivalent to %d hour(s) and %d minutes\n" %(totalMins, hours, mins))
                break
            else:
                print("\tThe minimum value for minutes should be 1")
    elif choice == "5":
        print("\tWelcome to temperature conversion")
        celciusTemp = getFloate("celcius temperature")
        fahTemp = float(celciusTemp) * 9 / 5 + 32
        print("\t" + str(round(celciusTemp, 2)), "°C is equivalent to", round(fahTemp, 2), "°F.\n")
    elif choice == "6":
        print("\tMarvin will print a word as many times as you would want.")
        word = input("\tEnter a word of your choice : ")
        factor = 0
        while factor < 1:
            factor = getInteger("the multiplication factor")
            if factor >= 1:
                print("\t %s will not be printed %d times" %(word, factor))
                for times in range(1, factor+1):
                    print("\t %d %s" %(times, word))
                break
            else:
                print("\tThe multiplication factor must be atleast 1")
    elif choice == "7":
        print("\tMarvin can generate random numbers within a range.")
        minNum = getInteger("lower range")
        maxNum = getInteger("upper range")
        while maxNum < minNum:
            print("\tYou seem to have a upper range less than the lower range!")
            maxNum = getInteger("upper range")
        print("\tPrinting 10 random numbers between %d and %d ..." %(minNum, maxNum))
        for i in range(10):
            ranNum = random.randint(minNum, maxNum)
            print(ranNum, end=", ")
        print("\n")

    elif choice == "8":
        print("\tMarvin will help you calculate sum and average of your number series.")
        numSum = 0
        counter = 0
        num = None

        while True:
            userInput = input("\tEnter a number. Type 'done' to quit: ")
            if userInput == "done":
                break
            try:
                num = float(userInput)
            except ValueError:
                print("\tInvalid input")
                continue

            numSum += int(num)
            counter += 1
        print("\n\tStatistics:\n\t" + 20 * "-")
        print("\tThe sum of the %d numbers is " %counter, numSum)
        print("\tThe average number of these is", round(numSum/counter, 2))

    elif choice == "9":
        print("\tArea of a circle calculator.\n")

        while True:
            radius = getFloate("radius[cm]")
            if radius > 0:
                area = math.pi * radius * radius
                print("\tArea of circle with radius", round(radius, 2), "cm is", round(area, 2), "sq. cm")
                break
            else:
                print("\tRadius cannot be less than or equal to zero")
    elif choice == "10":
        print("\tMarvin will now calculate the hypotenus of a triangle.\n")
        while True:
            sideA = getFloate("side a[cm]")
            sideB = getFloate("side b[cm]")
            if sideA > 0 and sideB > 0:
                hypotenus = math.sqrt(sideA*sideA + sideB*sideB)
                print("\tThe hypotenus of the right-angled triangle with sides\n\t",
                      round(sideA, 2), "cm and ", round(sideB, 2), "cm is", round(hypotenus, 2), "cm")
                break
            else:
                print("\tNone of the sides should be <= 0!")

    elif choice == "11":
        print("\tThe number comparison game. Enter 'done' to end the game")

        current = None

        while True:
            userInput = input("\tEnter a number. Enter 'done' to quite : ")
            if userInput == "done" or userInput == "DONE":
                print("\tThanks for your time.")
                break
            try:
                num = float(userInput)
            except ValueError:
                print("\tI expect an integer ")

            if current is None:
                current = num

            elif num == current:
                print("\n\t", num, "is equal to", current)

            elif num > current:
                print("\t", num, "is larger than", current)
                current = num

            elif num < current:
                print("\t", num, "is smaller than", current)
                current = num

        # print("\tThe largest of the numbers is:", large)
        # print("\tThe smallest of the numbers is:", small)

    else:
        print("\tThat is not a valid choice. You can only choose from the menu.")

    input("\n\tMarvin can do more. Press enter to continue...")
