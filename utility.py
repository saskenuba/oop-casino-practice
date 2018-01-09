#!/usr/bin/env python
"""utility.py: All the utility classes we use around the casino,
such as the nonrandom function"""

import random


class NonRandom(random.Random):
    """A class to generate not so random numbers. Pick a seed and it will
    chose that seed as the next number """

    def __init__(self):
        pass

    def setSeed(self, value):
        self.value = value

    def randomInt(self):
        return self.value

    def choice(self, sequence):
        return sequence[self.value]

    @staticmethod
    def _choice(sequence, seed):
        """Special case if we want to feed a existing seed."""
        return sequence[seed]
