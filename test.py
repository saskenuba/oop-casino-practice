""" File used for unittesting
"""

import unittest
from classes import Outcome, Bin, Wheel
from classes import NonRandom
from BinBuilder import BinBuilder


class GameTestCase(unittest.TestCase):
    def setUp(self):
        self.outcome1 = Outcome("15", 36)
        self.outcome2 = Outcome("16", 35)
        self.outcome3 = Outcome("00-1-3-5", 5)
        self.outcome4 = Outcome("1-3-5-12", 12)

        # creating wheel with random value
        self.rouletteWheel = Wheel(22)


class OutcomeTest(GameTestCase):
    def runTest(self):
        #self.assertEqual(self.outcome1, self.outcome2)
        self.assertNotEqual(self.outcome3, self.outcome2)


class BinTest(GameTestCase):
    def runTest(self):
        zero = Bin(self.outcome1, self.outcome2)
        zerozero = Bin(self.outcome3)
        lowTwelve = Bin(self.outcome1, self.outcome3)
        self.assertIsInstance(zero, Bin)
        self.assertIsInstance(zerozero, Bin)
        print(lowTwelve)


class WheelTest(GameTestCase):
    def runTest(self):
        self.rouletteWheel.addOutcome(5, Outcome("1-3-4", 24))
        self.rouletteWheel.addOutcome(1, self.outcome2)
        self.rouletteWheel.addOutcome(22, self.outcome1)
        self.assertIsInstance(self.rouletteWheel.bins[5], Bin)
        print(self.rouletteWheel.get(22))


class BinBuilderTest(GameTestCase):
    def runTest(self):
        BinBuilder(self.rouletteWheel)
        print(self.rouletteWheel.get(4))


testCase = OutcomeTest()
testCase = BinTest()
testCase = WheelTest()
testCase = BinBuilderTest()

if __name__ == '__main__':
    unittest.main()
