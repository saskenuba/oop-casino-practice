#!/usr/bin/env python
"""utility.py: All the utility classes we use around the casino,
such as the nonrandom function"""

import random

# TODO: the main is failing because we run out of predictable outcomes,
# so try to setup a pattern


class NonRandom(random.Random):
    """A class to generate not so random numbers. Pick a seed and it will
    chose that seed as the next number

    eachOfSequence: returns on every call a predictable value from a list,
    consisting of [seed, seed, seed, seed+1, seed+1, seed+2] """

    def __init__(self):
        pass

    def setSeed(self, value):
        self.value = value
        self.listOfValues = [
            self.value, self.value, self.value, self.value + 1, self.value + 1,
            self.value + 1, self.value + 2
        ]

    def setCustomSequence(self, sequence):
        self.listOfValues = sequence

    def randomInt(self):
        return self.value

    def choice(self, sequence):
        return sequence[self.value]

    def eachOfSequence(self):
        for value in self.listOfValues:
            yield value

    @staticmethod
    def _choice(sequence, seed):
        """Special case if we want to feed a existing seed."""
        return sequence[seed]
