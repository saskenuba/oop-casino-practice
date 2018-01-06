""" File used for unittesting
"""

import unittest
from classes import Outcome, Bin


class OutcomeTest(unittest.TestCase):
    def runTest(self):
        outcome1 = Outcome("hehe", 15)
        outcome2 = Outcome("hehe", 4)
        outcome3 = Outcome("affem", 9)
        self.assertEqual(outcome1, outcome2)
        self.assertNotEqual(outcome3, outcome2)
        print(outcome2.winAmount(4))


class BinTest(unittest.TestCase):
    def runTestBin(self):
        outcome1 = Outcome("rsrs", 15)
        outcome2 = Outcome("hehe", 4)
        outcome3 = Outcome("sacanage", 9)
        zero = Bin(outcome1, outcome2)
        zerozero = Bin(outcome3)
        self.assertIs(zero, Bin)
        self.assertIs(zerozero, Bin)
        print(zero)


if __name__ == '__main__':
    unittest.main()
