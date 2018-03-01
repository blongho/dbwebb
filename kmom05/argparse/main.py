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
sys.path.append("../analyzer/")
import analyzer
import cli_parser


#sys.path.insert(0, "../analyzer")


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
        analyzer.show_silent(command, "../analyzer/" + fil, number)
    elif verbose:
        analyzer.show_verbose(command, "../analyzer/" + fil, number)
    else:
        analyzer.show_default(command, "../analyzer/" + fil, number)

    sys.exit()


if __name__ == "__main__":
    main()
