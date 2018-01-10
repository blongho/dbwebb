#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Bernard Che Longho, 2017-09-29
A file containning some quotations.
This file has 3 code snippets
    1. Today"s quote is give from some pre-defined quotes read from a file
       This quote works if user enters the word "citat" in the terminal
    2. Quote about lunch
        If user enters the word "lunch", then lunch quotes are called
    3. If user enters the word "hej", or "hi", or "hellow", the marvin will
       send a greeting back.
All interactions take place at the terminal in clear text
"""

# ==========================================================================
# ==========================================================================
import random

# the quote of the day
def quote_of_today():
    """
    Reads quotations from the file quotes.txt and presents it if the user
    enters a word that contains "citat" (upper of lower case)
    """
    fname = "quotes.txt"
    lines = open(fname).read().splitlines()
    myQuote = random.choice(lines)

    print("\t" + myQuote)

# ==========================================================================
# ==========================================================================

def greet_marvin():
    """
    Marvin greets the user back if the user says hi, or hello, or hey
    """
    mgs = ["Yes, what can i do for you?", "Let me help you from your huddles.",
           "Excuse me, what do you want?", "Can i help you?",
           "I can answer all of your questions.", "Give me hi-five!",
           "Hi dear, what do you want today?", "Oh, sorry, i erred again. What happened!",
           "I am answerable only to Mos, he is my heroe", "Mos is the king."]
    msg_no = len(mgs)
    ran_num = random.randint(0, msg_no-1)
    print("\t" + mgs[ran_num])

# ==========================================================================
# ==========================================================================

def lunch_quotes():
    """
    If user enters "lunch", something about lunch is printed
    """
    lunch = ["Shall we go for lunch at %s?",
             "I am thinking of going out to %s. Will you follow?",
             "It is cosy at %s, shall we go?",
             "Today i am taking luch at %s at the job side.",
             "People say at %s they cook good food."]

    lunch_loc = ["Indiska", "Pasterian", "Villa Oscar", "Freds", "mcDonalds",
                 "subway", "kinabuffé på Cats", "valentino", "lotterilådan",
                 "casablance", "infinity", "östervärn", "argentina"]

    ran_lunch = lunch[random.randint(0, (len(lunch) - 1))]
    loc = lunch_loc[random.randint(0, (len(lunch_loc) - 1))]

    print("\t" + ran_lunch %loc)
