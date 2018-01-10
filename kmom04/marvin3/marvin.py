#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Marvin with a simple menu to start up with.
Marvin doesnt do anything, just presents a menu with some choices.
You should add functinoality to Marvin.
"""
import random
import math
import datetime

from inventory import manage_inventory
import quotes
# ==========================================================================
# ==========================================================================
def runMarvin():
    """
    Contains the menu phase of the marvin program
    Its an eternal loop, until q is pressed.
    It should check the choice done by the user and call a appropriate
    function.
    """
    while True:
        i = datetime.datetime.now()
        print(chr(27) + "[2J" + chr(27) + "[;H")
        print(marvin_image)
        showMenu()

        print("\tSystem now: {t}\n".format(t=i.strftime("%a, %x %X")))

        choice = input("\tChoice from menu >>> ")

        lower_ch = choice.lower()


        if lower_ch == "q" or lower_ch == "bye" or lower_ch == "done":
            goodBye()
            break

        elif "citat" in choice.lower():
            quotes.quote_of_today()

        elif "inv" in lower_ch:
            manage_inventory(choice)

        elif "hi" in lower_ch or "hello" in lower_ch or "hej" in lower_ch:
            quotes.greet_marvin()

        elif "lunch" in lower_ch:
            quotes.lunch_quotes()

        elif choice == "2":
            personLifeTimeInSeconds()

        elif choice == "3":
            calculateMoonWeight()

        elif choice == "4":
            minsToHourMin()

        elif choice == "5":
            celciusToFahrenheit()

        elif choice == "6":
            multiplyWord()

        elif choice == "7":
            randomNumGenerator()

        elif choice == "8":
            sumAndAvgInNumSeries()

        elif choice == "9":
            areaOfCircle()

        elif choice == "10":
            calHypotenus()

        elif choice == "11":
            numComparison()

        elif choice == "12":
            guessMyNumber(1, 100, 6)

        elif choice == "13":
            wordShuffle()

        elif choice == "14":
            nowAndMood()

        elif choice == "15":
            gradePoint()

        else:
            print(invalidChoice() %choice)

        re_run()


# ==========================================================================
# ==========================================================================
def getInteger(someString):
    """
    a function that takes and validates an integer
    The function takes a string that tells the user what to enter and returns
    an integer
    """
    while True:
        inp = input("\n\tEnter the value for %s: " %someString)
        try:
            value = int(inp)
            break
        except ValueError:
            print("\t'%s' is not a valid input here!" %inp)
    return value
# ==========================================================================
# ==========================================================================

def getFloate(someString):
    """
    a function that takes and validates a float
    The function takes a string that tells the user what to enter and returns
    a valid float. Until such is valid, the user keeps on getting the question
    After three unsuccessful tries, the use is sent out.
    """
    while True:
        inp = input("\n\tEnter the value for %s: " %someString)
        try:
            value = float(inp)
            break
        except ValueError:
            print("\t'%s' is not a number!" %inp)
    return value

# ==========================================================================
# ==========================================================================

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
# ==========================================================================
# ==========================================================================

def showMenu():
    """
    Prints the marvin menu |
    """
    print("\tHi, I'm Marvin. I know it all. What can I do you for?")
    print("\n\tPick a number from the menu")
    print("\t" + 40 * '-')
    print("\t1)  Present yourself to Marvin.")
    print("\t2)  Get your age in seconds.")
    print("\t3)  Get your weight on the moon.")
    print("\t4)  Convert minutes to hours.")
    print("\t5)  Celcius to fahrenhet converter.")
    print("\t6)  Word multiplication.")
    print("\t7)  Random number generator.")
    print("\t8)  Sum and average of numbers.")
    print("\t9  (extra)) Calculate the area of a circle.")
    print("\t10 (extra)) Calculate hypotenus of a right-angled triangle.")
    print("\t11 (extra)) Number comparisom game.")
    print("\t12) Guess a number game.")
    print("\t13) Word shuffling.")
    print("\t14 (extra)) Show current date, time and other data.")
    print("\t15) Grade point calculator.")
    print("\tQ)  Quit.")
    print("\t" + 40 * '-')

# ==========================================================================
# ==========================================================================

def goodBye():
    """
    Print a goodby message when the user enters q
    """
    print("\tBye, bye - and welcome back anytime!")

# ==========================================================================
# ==========================================================================

def greetUser():
    """
    Asks a user's name and print a message
    """
    name = None
    while name is None:
        name = input("\tWhat is your name? : ")

    print("\n\tMarvin says:\n")
    print("\tHello %s - your awesomeness!" % name)

# ==========================================================================
# ==========================================================================

def personLifeTimeInSeconds():
    """
    A program that takes a person's age, calculates the time that person
    has spent on earth in seconds and prints the result
    Program checks that age is integer and that it is atleast 1
    """
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

# ==========================================================================
# ==========================================================================

def calculateMoonWeight():
    """
    A program that asks for a weight in kg, then gives the equivalent
    weight in the moon
    Program only presents equivalent weight when user enters a valid weight
    greater than 0
    """
    print("\tMarvin can convert any weight to its equivalent in the moon.\n")

    earthWeight = 0
    while earthWeight < 1:
        earthWeight = getInteger("weight[kg]")

        if earthWeight > 0:
    # from http://www.learningaboutelectronics.com/Articles/Weight-on-the-moon-conversion-calculator.php#answer
            moonWeight = float((earthWeight / 9.81) * 1.622)

            print("\tThe weight of %d kg on earth is equivalent to"\
                %earthWeight, round(moonWeight, 2), "kg on the moon.\n")
        else:
            print("\tWeight must be greater than 0!")

# ==========================================================================
# ==========================================================================

def minsToHourMin():
    """
    Program to convert time from minutes to hh:mm
    """
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

# ==========================================================================
# ==========================================================================

def celciusToFahrenheit():
    """
    Converts celcius temperature to fahrenheit
    """
    print("\tWelcome to temperature conversion")

    celciusTemp = getFloate("celcius temperature")

    fahTemp = float(celciusTemp) * 9 / 5 + 32

    print("\t" + str(round(celciusTemp, 2)) + " °C is equivalent to " + str(round(fahTemp, 2)) + " °F.\n")

# ==========================================================================
# ==========================================================================

def multiplyWord():
    """
    Multiply a user-defined word a number of user-defined times
    """
    print("\tMarvin will print a word as many times as you would want.")

    word = input("\tEnter a word of your choice : ")

    factor = 0

    while factor < 1:
        factor = getInteger("the multiplication factor")
        if factor >= 1:
            print("\t%s will not be printed %d times" %(word, factor))

            for times in range(1, factor+1):
                print("\t%d %s" %(times, word))
            break
        else:
            print("\tThe multiplication factor must be atleast 1.")

# ==========================================================================
# ==========================================================================

def randomNumGenerator():
    """
    Generates 10 random numbers in a range specified by the user
    """
    print("\tMarvin can generate random numbers within a range.")

    minNum = getInteger("lower range")
    maxNum = getInteger("upper range")

    while maxNum < minNum or maxNum == minNum:
        print("\tThe value for the max range must be large than lower range!")
        maxNum = getInteger("upper range")

    print("\n\tPrinting 10 random numbers between %d and %d ..." %(minNum, maxNum))

    strNum = ""

    for _ in range(10):
        ranNum = random.randint(minNum, maxNum)
        strNum += str(ranNum) + ","

    print("\t %s" %strNum)

# ==========================================================================
# ==========================================================================

def sumAndAvgInNumSeries():
    """
    Takes a series of number until user types done.
    Returns the sum and the average of the numbers
    """
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
            print("\tInvalid input. I expect a number e.g 1, 2, ...")
            continue

        numSum += int(num)
        counter += 1

    print("\n\tStatistics:\n\t" + 20 * "-")
    print("\tThe sum of the %d numbers is " %counter, numSum)
    print("\tThe average of these numbers is ", round(numSum/counter, 2))

# ==========================================================================
# ==========================================================================

def areaOfCircle():
    """
    Takes a valid value for the radius of a circle and prints the area
    """
    print("\tArea of a circle calculator.\n")

    while True:
        radius = getFloate("radius[cm]")

        if radius > 0:
            area = math.pi * radius * radius

            print("\tArea of circle with radius", round(radius, 2), "cm is",
                  round(area, 2), "sq. cm")
            break

        else:
            print("\tRadius cannot be less than or equal to zero")
# ==========================================================================
# ==========================================================================

def calHypotenus():
    """
    Calculates the hypotenus of a right-angled triangle from two of its sides
    """
    print("\tMarvin will now calculate the hypotenus of a triangle.\n")
    while True:
        sideA = getFloate("side a[cm]")
        sideB = getFloate("side b[cm]")

        if sideA > 0 and sideB > 0:
            hypotenus = math.sqrt(sideA*sideA + sideB*sideB)

            print("\tThe hypotenus of the right-angled triangle with sides\n")
            print("\t", round(sideA, 2), "cm and", round(sideB, 2), "cm is",
                  round(hypotenus, 2), "cm")

            break
        else:
            print("\tNone of the sides should be <= 0!")

# ==========================================================================
# ==========================================================================

def numComparison():
    """
    Compares each number a user enters with the previous one and says
    if the number is equal, less than or greater than the previos one
    """
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
# ==========================================================================
# ==========================================================================
def invalidChoice():
    """
    Prints message telling the user that the choice is wrong
    """
    return "\t'%s' is not a valid choice. You can only choose from the menu."
# ==========================================================================
# ==========================================================================

def re_run():
    """
    Print message telling the user that program can be re-run
    """
    input("\n\tPress enter to continue...")

# ==========================================================================
# ==========================================================================

def guessMyNumber(num1, num2, tries):
    """
    Program asks the user to guess a randomly generated number between 1
    and 100.
    Program compares user input with generated number and says if the user
    wins (i.e guessed rightly) or the number is bigger or smaller.
    User has max of 6 tries before the program ends

    Edit 2017-09-20:
        Added inparameters so that the program can be customized by the user.
        i.e the user can now specify the number range and the number of times s(he) can do the tries.
    """
    print("\tThe number guessing game...")

    if abs(num1 - num2) < (2 * tries): # make sure the range is big enough.
        print("\tOops! The range is too close compared to the tries.")
    else:
        # make sure limits are right
        low = num1 if num1 < num2 else num2
        high = num1 if num1 > num2 else num2

        secretNum = random.randint(low, high)

        maxGuess = 0
        guessNum = 0
        print("\tI am thinking of a number between {lo} and {hi}. Can you guess\
              it? (You have {tr} trials)".format(lo=low, hi=high, tr=tries))
        while maxGuess < tries:

            guessNum = getFloate("trial #{t}".format(t=(maxGuess+1)))

            if guessNum < low or guessNum > high:
                print("\tPlease enter a number between {lo} and {hi}".format(lo=low, hi=high))
                continue

            maxGuess += 1

            if guessNum > secretNum:
                print("\t%d is too high" %guessNum)
            elif guessNum < secretNum:
                print("\t%d is too low." %guessNum)
            elif guessNum == secretNum:
                break

        if guessNum == secretNum:
            print("\n\tCongratulations! You guessed the right number after %d tries"
                  %maxGuess)

        if guessNum != secretNum:
            print("\n\tSorry :( maximum trials reached! The number was %d" %secretNum)


# ==========================================================================
# ==========================================================================

def wordShuffle():
    """
    Takes a word and then shuffles its characters and prints the shuffled word
    """
    toShuffle = input("\tEnter a word and marvin will shuffle it: ")

    shuffled = "".join(random.sample(toShuffle, len(toShuffle)))

    print("\tShuffled '%s' to '%s'" %(toShuffle, shuffled))

# ==========================================================================
# ==========================================================================

def gradePoint():
    """
    A program to calculate the grade point of a user.
    It prints the grades according to the following criteria:
    Score   Grade
    >= 0.9   A
    >= 0.8   B
    >= 0.7   C
    >= 0.6   D
    < 0.6    F
    """
    print("\tMarvin will help you get your grade point.")
    grade = ""
    userGrade = getInteger("your points")
    maxPoint = getInteger("maximum possible point")

    while maxPoint < userGrade:
        print("\tMax point cannot be < your point.")
        maxPoint = getInteger("maximum possible point")

    percentage = userGrade / maxPoint

    if percentage >= 0.9:
        grade = "A"
    elif percentage >= 0.8 and percentage < 0.9:
        grade = "B"
    elif percentage >= 0.7 and percentage < 0.8:
        grade = "C"
    elif percentage >= 0.6 and percentage < 0.7:
        grade = "D"
    else:
        grade = "F"

    print("\n\tYour grade is: {gp}".format(gp=grade))

# ==========================================================================
# ==========================================================================


def nowAndMood():
    """
    Print a string with today's date and time, someone's mood and an integer
    and float that has something in common in the context
    """
    # modified time extration from using gmtime which gave time inconsistent
    # with system time

    moodFile = open("moods.txt")

    readline = moodFile.readline()

    mood = random.choice((readline).split())

    #computing date parameters
    i = datetime.datetime.now()

    år = i.strftime("%Y")
    mån = i.strftime("%B")
    mnthDay = i.strftime("%d")
    dag = i.strftime("%A")
    datNr = i.strftime("%j")
    veckorNr = i.strftime("%W")
    hr = i.strftime("%I")
    mins = i.strftime("%M")
    pm = i.strftime("%p")

    data = "{wday}, {dayn} {mon} {yr} {h}:{m} {p}, week {wkn} marks {days} days since the start of the year.".format(
        h=hr, m=mins, p=pm, wday=dag, dayn=mnthDay, mon=mån, yr=år, wkn=veckorNr, days=datNr)

    print("\tToday", data, "Are you {s}?".format(s=mood))

# ==========================================================================
# ==========================================================================
