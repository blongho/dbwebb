#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Bernard Longho, 2017-10-07
A program that reads and analyzes the contents of a file
"""
import string

fname = "phil.txt"

# ============================================================================
# ============================================================================


def file_stats(filname):
    """
    Reads a file
    Counts the lines, words and number of alphabetical characters
    """
    nlines = 0
    nwords = 0
    nchar = 0
    totchar = 0
    try:
        with open(filname, "r") as f:
            for line in f:
                totchar += sum(1 for c in line)
                word_list = line.split()
                nlines += 1
                nwords += len(word_list)
                nchar += sum(1 for c in line if c.isalpha())
        stats = {"lines": nlines,
                 "words": nwords,
                 "letters": nchar,
                 "characters": totchar}
        return stats
    except IOError:
        print("Unable to open '{fil}'.".format(fil=filname))

# ============================================================================
# ============================================================================


def remove_punctionation(ilist):
    """
    Takes a list of words(characters) and returns same without the punctuations
    """
    ilist = [''.join(c for c in s if c not in string.punctuation)
             for s in ilist]
    return ilist

# ============================================================================
# ============================================================================


def read_content(filname):
    """
    Takes a file name,
    Reads the file and return its content as a string fur further analyses
    """
    try:
        with open(filname, "r") as fil:
            content = fil.read()
        return content.lower()
    except IOError:
        print("Error reading '{file}'".format(file=filname))
        exit()

# ============================================================================
# ============================================================================


def letter_count(filname):
    """
    Counts alphabetical letters in a text file.
    Stores the frequency of each character in a dictionary.
    Returns the dictionary
    """
    letter_dict = dict()

    for line in read_content(filname):
        words = line.split()
        for char in words:
            if not str(char).isalpha():
                continue
            letter_dict[char] = letter_dict.get(char, 0) + 1

    return letter_dict

# ============================================================================
# ============================================================================


def word_count(filname):
    """
    Read a file
    Count the words and calculates their frequency
    """
    content = read_content(filname)

    word_list = content.split()
    word_list = remove_punctionation(word_list)

    word_dict = dict()

    for word in word_list:
        if not str(word).isalpha():
            continue
        word_dict[word] = word_dict.get(word, 0) + 1
    return word_dict

# ============================================================================
# ============================================================================


def verbose_freq(idic, itm, n=7, rsort=True):
    """
    Prints frequency statistics of word analyses
    inparameters:
        idic (dictionary of objects)
        n (integer definining how many items to be printed)
        default sort in ascending order
    """

    if rsort:
        print(
            "Showing data for the {} most frequent {} sorted in decending order.".format(n, itm))
    else:
        print(
            "Showing data for {} {} frequency sorted in ascending order.".format(
                n,
                itm))

    if itm == "letters":
        print("{:<8} {:<8} {:<10}".format(itm, "count", "percent"))
        print("-" * 28)
    elif itm == "words":
        print("{:<15} {:<8} {:<6}".format(itm, "count", "percent"))
        print("-" * 28)

    cnt = 0
    total = sum(idic.values())

    for item in sorted(idic, key=idic.get, reverse=rsort):
        val = idic.get(item)
        per = str(round(val / total * 100, 2)) + " %"
        if itm == "letters":
            print("{:<8} {:<8} {:<6}".format(item, val, per))
            cnt += 1
            if cnt == n:
                break
        elif itm == "words":
            print("{:<15} {:<8} {:<6}".format(item, val, per))
            cnt += 1
            if cnt == n:
                break
# ============================================================================
# ============================================================================


def show_silent(command, filname, num=7):
    """
    Defines how a silent output will display
    @param command [all|lines|words|letters|word_frequency|letter_frequency]
    @param filname file to read data from
    @return Depending on the command, returns the required data
    """
    info = ""
    stat = file_stats(filname)
    if command == "all":
        info = "Letters: {let}\nWords: {w}\nLines: {lin}".format(
            lin=stat["lines"],
            w=stat["words"],
            let=stat["letters"]
        )
        print(info)
    elif command == "lines":
        info = "Lines: {lin}".format(lin=stat["lines"])
        print(info)
    elif command == "words":
        info = "Words: {w}".format(w=stat["words"])
        print(info)
    elif command == "letters":
        info = "Letters: {l}".format(l=stat["letters"])
        print(info)
    elif command == "word_frequency":
        cnt = 0
        word_dict = word_count(filname)
        for item in sorted(word_dict, key=word_dict.get, reverse=True):
            val = word_dict.get(item)
            percent = str(round(val / stat["words"] * 100, 2)) + " %"
            print("{:<10} {:>8}".format(item, percent))
            cnt += 1
            if cnt == num:
                break
    elif command == "letter_frequency":
        cnt = 0
        let_dict = letter_count(filname)
        for char in sorted(let_dict, key=let_dict.get, reverse=True):
            val = let_dict.get(char)
            percent = str(round(val / stat["letters"] * 100, 2)) + " %"
            print("{:<3} {:>8}".format(char, percent))
            cnt += 1
            if cnt == num:
                break

# ============================================================================
# ============================================================================


def show_default(command, filname, num=7):
    """
    The default display
    @param command [all|lines|words|letters|word_frequency|letter_frequency]
    @param filname file to read data from
    @return Depending on the command, returns the required data
    """

    info = "'{}' contains\n".format(filname[filname.rfind("/") + 1:])
    stat = file_stats(filname)
    if command == "all":
        info += "Characters: {c}\nLetters: {let}\nWords: {w}\nLines: {lin}".format(
            lin=stat["lines"],
            w=stat["words"],
            let=stat["letters"],
            c=stat["characters"]
        )
        print(info)
    elif command == "lines":
        info += "Lines: {lin}".format(lin=stat["lines"])
        print(info)
    elif command == "words":
        info += "Words: {w}".format(w=stat["words"])
        print(info)
    elif command == "letters":
        info += "Letters: {l}".format(l=stat["letters"])
        print(info)
    elif command == "word_frequency":
        cnt = 0
        word_dict = word_count(filname)

        print("The {n} most frequent words in the file..".format(n=num))
        print("{:<10} {:>8}".format("words", "frequency"))
        print("-" * 20)

        for item in sorted(word_dict, key=word_dict.get, reverse=True):
            val = word_dict.get(item)
            percent = str(round(val / stat["words"] * 100, 2)) + " %"
            print("{:<10} {:>8}".format(item, percent))
            cnt += 1
            if cnt == num:
                break
    elif command == "letter_frequency":
        cnt = 0
        let_dict = letter_count(filname)

        print("The {n} most frequent letters in the file..".format(n=num))
        print("{:<10} {:>8}".format("letter", "frequency"))
        print("-" * 20)

        for char in sorted(let_dict, key=let_dict.get, reverse=True):
            val = let_dict.get(char)
            percent = str(round(val / stat["letters"] * 100, 2)) + " %"
            print("{:<10} {:>8}".format(char, percent))
            cnt += 1
            if cnt == num:
                break

# ============================================================================
# ============================================================================


def show_verbose(command, filname, num=7):
    """
    The default display
    @param command [all|lines|words|letters|word_frequency|letter_frequency]
    @param filname file to read data from
    @return Depending on the command, returns the required data
    """
    info = "'{}' contains\n".format(filname[filname.rfind("/") + 1:])
    stat = file_stats(filname)
    if command == "all":
        info += "Characters: {c}\nLetters: {let}\nWords: {w}\nLines: {lin}\nSentences: {sn}".format(
            lin=stat["lines"],
            w=stat["words"],
            let=stat["letters"],
            c=stat["characters"],
            sn=read_content(filname).count('.')
        )
        print(info)
    elif command == "lines":
        info += "Lines: {lin}".format(lin=stat["lines"])
        print(info)
    elif command == "words":
        info += "Words: {w}".format(w=stat["words"])
        print(info)
    elif command == "letters":
        info += "Letters: {l}".format(l=stat["letters"])
        print(info)
    elif command == "word_frequency":
        word_dict = word_count(filname)
        verbose_freq(word_dict, "words", num, True)

    elif command == "letter_frequency":
        let_dict = letter_count(filname)
        verbose_freq(let_dict, "letters", num, True)
# ============================================================================
# ============================================================================
