#!/usr/bin/env python3
# -*- coding: utf-8 -*-

"""
Main cli-program, to start it all up by reading command line
options and arguments and then executing whats to be executed.

See usage.py for details how to use program.
>>> import cli_parser
>>> help(cli_parser)

or

$ pydoc cli_parser

"""
import sys

import analyzer
import cli_parser

sys.path.append("../analyzer")



def main():
    """
    Main function where it all starts.
    """
    option = cli_parser.parse_options()
    command = option["known_args"]["commands"]
    silent = option["known_args"]["silent"] == True
    verbose = option["known_args"]["verbose"] == True
    number = option["known_args"]["amount"]
    fil = option["known_args"]["filename"]
    if silent:
        print("Silent printing")  # for debugging
        analyzer.show_silent(command, "../analyzer/" + fil, number)
    elif verbose:
        print("verbose printing")
        analyzer.show_verbose(command, "../analyzer/" + fil, number)
    else:
        print("default printing")
        analyzer.show_default(command, "../analyzer/" + fil, number)

    # lines
    # elif command == "lines":
    #     if silent:
    #         analyzer.show_silent("lines", "../analyzer/" + fil)
    #     elif verbose:
    #         analyzer.show_verbose("lines", "../analyzer/" + fil)
    #     else:
    #         analyzer.show_default("lines", "../analyzer/" + fil)
    # # words
    # elif command == "words":
    #     if silent:
    #         analyzer.show_silent("words", "../analyzer/" + fil)
    #     elif verbose:
    #         analyzer.show_verbose("words", "../analyzer/" + fil)
    #     else:
    #         analyzer.show_default("words", "../analyzer/" + fil)
    # # letters
    # elif command == "letters":
    #     if silent:
    #         analyzer.show_silent("letters", "../analyzer/" + fil)
    #     elif verbose:
    #         analyzer.show_verbose("letters", "../analyzer/" + fil)
    #     else:
    #         analyzer.show_default("letters", "../analyzer/" + fil)
    # # word_frequency
    # elif command == "word_frequency":
    #     if silent:
    #         analyzer.show_silent("word_frequency", "../analyzer/" + fil)
    #     elif verbose:
    #         analyzer.show_verbose("word_frequency", "../analyzer/" + fil)
    #     else:
    #         analyzer.show_default("word_frequency", "../analyzer/" + fil)
    # # letter frequency
    # elif command == "letter_frequency":
    #     #amt = opt["known_args"]["amount=<integer>"]
    #     if silent:
    #         analyzer.show_silent("letter_frequency", "../analyzer/" + fil)
    #     elif verbose:
    #         analyzer.show_verbose("letter_frequency", "../analyzer/" + fil)
    #     else:
    #         analyzer.show_default("letter_frequency", "../analyzer/" + fil)

    # print(option["unknown_args"])
    # print(option["known_args"]["commands"])
    # print(option)
    # print(cli_parser.options)

    # print(cli_parser.options["known_args"]["command"])

    # print()

    sys.exit()


if __name__ == "__main__":
    main()
