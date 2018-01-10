#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Parse CLI options.

Using argparse to parse options.
"""
import argparse
import os
import sys

PROGRAM = os.path.basename(sys.argv[0])
AUTHOR = "Bernard Che Longho"
EMAIL = "lobe16@student.bth.se"
VERSION = "v1.0.0 (2017-10-07)"

# =============================================================================
# =============================================================================


def info():
    """Print usage information about the script."""
    return "Author: {author} | <{email}>".format(
        author=AUTHOR, email=EMAIL)

# =============================================================================
# =============================================================================


def add_options(parser):
    """
    Add options for the parser
    """
    group = parser.add_mutually_exclusive_group()

    group.add_argument("-v", "--verbose", dest="verbose", default="False",
                       help="More output", action="store_true")
    group.add_argument("-s", "--silent", dest="silent", default="False",
                       help="Less output", action="store_true")

    owner_group = parser.add_mutually_exclusive_group()

    owner_group.add_argument("-V", "--version",
                             action="version",
                             version=VERSION)
    owner_group.add_argument("-a, --author", action="version",
                             help="Show author information",
                             version=info())

    parser.add_argument("-amt", "--amount", type=validAmount, default=7,
                        help="Number of words or letters to display freq (>=7)")

# =============================================================================
# =============================================================================


def add_commands(parser):
    """
    Add commands for the cli program
    """
    subparsers = parser.add_subparsers(title="Commands(positional arguments)",
                                       help="Available commands",
                                       dest="commands")

    subparsers.add_parser(
        "all", help="<options> [all] [file] Summarized statistics <file>")
    subparsers.add_parser(
        "lines",
        help="<options> [lines] [file] Number of lines <file>")

    subparsers.add_parser(
        "words",
        help="<options> [words] [file] Number of word in <file>")

    subparsers.add_parser(
        "letters",
        help="<options> [letters] [file] Number of letters in <file>")

    subparsers.add_parser(
        "word_frequency",
        help="<options> [word_frequency] [file] Frequency table of words in <file>")

    subparsers.add_parser(
        "letter_frequency",
        help="<options> [letter_frequency] [file] Frequency table of letters in <file>")
    parser.add_argument("filename", help="The file to read data from")


# =============================================================================
# =============================================================================
def parse_options():
    """
    Parse all command line options and arguments and return them as a dictionary.
    """
    # parser = argparse.ArgumentParser(formatter_class=argparse.RawTextHelpFormatter)

    parser = argparse.ArgumentParser()

    add_commands(parser)
    add_options(parser)
    args, unknown_args = parser.parse_known_args()

    options = {}

    options["known_args"] = vars(args)
    options["unknown_args"] = unknown_args
    # print("Printing unknownargs ")
    # print(options["unknown_args"])
    # print("Printing known options")
    # print(options["known_args"])
    # print(args)
    return options

# =============================================================================
# =============================================================================


def validAmount(number):
    """
    Validate the number entered in argparse
    number should be integer>=7
    """
    value = int(number)
    if value < 7:
        raise argparse.ArgumentTypeError("Minimum value for amount is 7")
    return value
