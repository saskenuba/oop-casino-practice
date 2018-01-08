#!/usr/bin/env python
"""utility.py: All the utility classes we use around the casino,
such as the nonrandom function"""

import random


class NonRandom(random.Random):
    """A class to generate not so random numbers. Pick a seed and it will
    chose that seed as the next number """

    def __init__(self):
        self.value = 0

    def setSeed(self, value):
        self.value = value
        return self.value

    def choice(self, sequence):
        return sequence[self.value]
