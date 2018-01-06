#!/usr/bin/env python
"""Foobar.py: Here we find the classes of the casino."""

__author__ = "Martin Mariano"
__copyright__ = "Copyright 2018, Planet Earth"

import random


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

    def __hash__(self):
        return 0


class Bin():
    def __init__(self, *outcomes):
        self.outcomes = frozenset(outcomes)

    def __str__(self):
        'Easy to check representation of the outcomes'
        return ", ".join(map(str, self.outcomes))

    def outcomes(self):
        return self.outcomes

    def add(self, outcome):
        """ Adds a new outcome to the frozenset
        """
        self.outcomes |= frozenset([outcome])


class Wheel():
    def __init__(self, rng):
        "This contains the 38 bins of the Roulette, and a random number generator to \
        generate outcomes"

        self.bins = tuple(Bin() for i in range(38))
        self.rng = rng

    def addOutcome(self, binNumber, outcome):
        self.bins[binNumber].add(outcome)

    def next(self):
        """Selects a random bin from 0 to 37, and returns it."""
        return random.choice(self.bins)

    def get(self, index):
        """Returns desired Bin"""
        return self.bins[index]


class NonRandom(random.Random):
    def __init__(self):
        self.value = 0

    def setSeed(self, value):
        self.value = value
        return self.value

    def choice(self, sequence):
        return sequence[self.value]
