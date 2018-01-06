#!/usr/bin/env python
"""Foobar.py: Here we find the classes of the casino."""

__author__ = "Martin Mariano"
__copyright__ = "Copyright 2018, Planet Earth"


class Outcome():
    def __init__(self, name, odds):
        self.name = name
        self.odds = odds

    def winAmount(self, amount):
        'Calculate the amount of winnings'
        return self.odds * amount

    def __eq__(self, other):
        'Returns true if names match with same object'
        return self.name == other

    def __ne__(self, other):
        return self.name != other

    def __str__(self):
        'Easy to see representation of outcome'
        return '{} ({}:1)'.format(self.name, self.odds)


class Bin():
    def __init__(self, *outcomes):
        self.outcomes = frozenset(outcomes)

    def __str__(self):
        return ", ".join(map(str, self.outcomes))
