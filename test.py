""" File used for unittesting
"""

import unittest
from classes import Outcome, Bin, Wheel, Bet, Table
from roulette import RouletteGame
from player import Passenger57
from BinBuilder import BinBuilder
from exceptions import InvalidBet


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
        self.assertIsInstance(self.outcome1, Outcome)
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
        BinBuilder(self.rouletteWheel)
        self.rouletteWheel.addOutcome(5, Outcome("1-3-4", 24))
        self.rouletteWheel.addOutcome(1, self.outcome2)
        self.rouletteWheel.addOutcome(22, self.outcome1)
        self.assertIsInstance(self.rouletteWheel.bins[5], Bin)
        """This is also testing getting the outcome from the wheel
        and placing a bet on it"""
        myOutcome = self.rouletteWheel.getOutcome('Street 4-5-6')
        myBet = Bet(10, myOutcome)
        print(myBet)
        print(myBet.winAmount())


class BinBuilderTest(GameTestCase):
    def runTest(self):
        BinBuilder(self.rouletteWheel)
        print(self.rouletteWheel.next())


class BetTest(GameTestCase):
    def runTest(self):
        BinBuilder(self.rouletteWheel)
        outcome5 = Outcome('Number 25', 35)
        newBet = Bet(25, outcome5)
        print(newBet.winAmount())
        print(newBet.loseAmount())


class TableTest(GameTestCase):
    def runTest(self):
        BinBuilder(self.rouletteWheel)
        currentTable = Table()
        currentTable.Table()

        myOutcome = self.rouletteWheel.getOutcome('Split 5-6')
        myBet = Bet(10, myOutcome)
        myOutcome2 = self.rouletteWheel.getOutcome('Number 1')
        myBet2 = Bet(191, myOutcome2)
        currentTable.placeBet(myBet)
        """Exception needs to be raised because the bet exceeds the table limit"""
        with self.assertRaises(InvalidBet):
            currentTable.placeBet(myBet2)

        myOutcome3 = self.rouletteWheel.getOutcome('Black Bet')
        myBet3 = Bet(75, myOutcome3)
        currentTable.placeBet(myBet3)

        activeBets = [x.outcome.name for x in currentTable.__iter__()]
        print(activeBets)


class RouletteGameTest(GameTestCase):
    def runTest(self):
        BinBuilder(self.rouletteWheel)
        currentTable = Table()
        currentTable.Table()

        player = Passenger57(currentTable, self.rouletteWheel)
        game = RouletteGame(self.rouletteWheel, currentTable)
        game.cycle(player)


testCase = OutcomeTest()
testCase = BinTest()
testCase = WheelTest()
testCase = BinBuilderTest()
testCase = BetTest()
testCase = TableTest()
testCase = RouletteGameTest()

if __name__ == '__main__':
    unittest.main()
