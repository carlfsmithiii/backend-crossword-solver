#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""Crossword Solver Program"""

__author__ = "???"

import re

# YOUR HELPER FUNCTION GOES HERE


def main():
    with open('dictionary.txt') as f:
        words = f.read().split()

    test_word = raw_input(
        'Please enter a word to solve.\nUse spaces to signify unknown letters: ').lower()
    

    # YOUR ADDITIONAL CODE HERE
    regex = test_word.replace(r' ', r'\w') + r'$'
    matches = [word for word in words if re.match(regex, word)]
    for match in matches:
        print(match)

if __name__ == '__main__':
    main()
