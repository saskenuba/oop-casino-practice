import unittest
from classes import Outcome, Bin, Wheel, Bet, Table
from roulette import RouletteGame
from player import Passenger57, Martingale
from binbuilder import BinBuilder
from exceptions import InvalidBet, PlayerError
from utility import NonRandom


class GameTestCase(unittest.TestCase):
    def setUp(self):
        # creating wheel with nonrandom value
        notSoRandom = NonRandom()
        notSoRandom.setSeed(35)

        self.rouletteWheel = Wheel()
        BinBuilder(self.rouletteWheel)

        self.currentTable = Table()
        self.currentTable.Table(self.rouletteWheel)


class Passenger57Test(GameTestCase):
    def hehe(self):
        playerPassenger = Passenger57(self.currentTable)
        game = RouletteGame(self.rouletteWheel, self.currentTable)

        while True:
            try:
                game.cycle(playerPassenger, 0)
            except InvalidBet as betError:
                self.assertIsInstance(betError, InvalidBet)
                break
            except PlayerError as playerError:
                self.assertIsInstance(playerError, PlayerError)
                break


class MartingaleTest(GameTestCase):
    def runTest(self):
        playerPassenger = Martingale(self.currentTable)
        game = RouletteGame(self.rouletteWheel, self.currentTable)

        while True:
            try:
                game.cycle(playerPassenger, 0)
            except InvalidBet as betError:
                self.assertIsInstance(betError, InvalidBet)
                break
            except PlayerError as playerError:
                self.assertIsInstance(playerError, PlayerError)
                break
