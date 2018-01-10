#!/usr/bin/env python
"""classes.py: Here we find all the base classes for the games at the
casino to work"""

__author__ = "Martin Mariano"
__copyright__ = "Copyright 2018, Planet Earth"

import random
from exceptions import InvalidBet
from utility import NonRandom


class Outcome():
    """This class is responsible for containing the odds on determined outcome.

       Ex: Number 1 (35 odds to 1)

    """

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
    """Contains all the possible outcomes at a determined bin."""

    def __init__(self, *outcomes):
        self.outcomes = frozenset(outcomes)

    def __str__(self):
        'Easy to check representation of the outcomes'
        return ", ".join(map(str, self.outcomes))

    def outcomes(self):
        """Getter for outcomes"""
        return self.outcomes

    def add(self, outcome):
        """ Adds a new outcome to the frozenset """
        self.outcomes |= frozenset([outcome])


class Wheel():
    """This contains the 38 bins of the Roulette, and a random number generator to
        generate outcomes

    The wheel now has a functional nonrandom gen for testing purposes.

    """

    def __init__(self, rng=None):
        self.bins = tuple(Bin() for i in range(38))
        self.rng = rng  # if rng is not None else random.Random()
        self.AllOutcomesMap = set()

    def addToMap(self, outcome, binNumber):
        """This adds the current outcome NAME to the collection
           containing all outcomes"""
        self.AllOutcomesMap |= set([outcome])

    def addOutcome(self, binNumber, outcome):
        """Adds the outcome to the map and also to the designated bin"""
        self.addToMap(outcome, binNumber)
        self.bins[binNumber].add(outcome)

    def getOutcome(self, outcomeName):
        """Getter for selecting an arbitrary outcome from outcomes map"""
        for oc in self.AllOutcomesMap:
            if oc.name.lower() in outcomeName.lower():
                return oc

    def next(self):
        """Selects a random bin from 0 to 37, and returns it."""
        if self.rng is None:
            return random.choice(self.bins)
        return NonRandom._choice(self.bins, self.rng)

    def get(self, index):
        """Returns desired Bin"""
        return self.bins[index]


class Bet():
    "Allows betting a specific amount to a specific outcome"

    def __init__(self, amount, outcome):
        self.amount = amount
        self.outcome = outcome

    def __str__(self):
        return '{} on {}'.format(self.amount, self.outcome)

    def winAmount(self):
        """Calculates the winnings on outcome"""
        return self.outcome.winAmount(self.amount)

    def loseAmount(self):
        return self.amount


class Table():
    """Used to contain all the bets created by the player."""

    def __init__(self):
        pass

    def Table(self, wheel):
        """Has the currently active bets and the limit of the table"""
        self.betLimit = 200
        # TODO: Check if bet minimum is needed
        self.betMinimum = 5
        self.activeBets = []
        self.currentWheel = wheel

    def __iter__(self):
        return self.activeBets[:]

    def _isValid(self, bet):
        """Returns a boolean if the sum of all bets is less
        or equal to the table limit, and bet meets the table minimum."""
        total = int()
        for currentBets in self.activeBets:
            total += currentBets.amount
        return ((total + bet.amount) <=
                self.betLimit) and bet.amount >= self.betMinimum

    def clearAllBets(self):
        return self.activeBets.clear()

    def placeBet(self, bet):
        """Add bet to list of working bets, after checking for validity

        Returns 1 if bet was placed successfully.
        """
        if self._isValid(bet):
            self.activeBets.append(bet)
            return 1
        else:
            raise InvalidBet(
                'The bet of {} exceeds the table limit of {}'.format(
                    bet.amount, self.betLimit))
