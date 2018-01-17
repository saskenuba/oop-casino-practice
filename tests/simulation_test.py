import unittest
from classes import Outcome, Bin, Wheel, Bet, Table
from roulette import RouletteGame
from simulator import Simulator
from player import Passenger57, Martingale
from binbuilder import BinBuilder
from exceptions import InvalidBet, PlayerError
from utility import NonRandom


class test_Game(unittest.TestCase):
    def setUp(self):
        # creating wheel with nonrandom value
        notSoRandom = NonRandom()
        notSoRandom.setSeed(32)
        notSoRandom.setCustomSequence([32, 32, 32, 32, 32, 32, 32, 33])

        self.rouletteWheel = Wheel(notSoRandom)
        BinBuilder(self.rouletteWheel)

        self.currentTable = Table()
        self.currentTable.Table(self.rouletteWheel)

    def test_Roulette(self):
        game = RouletteGame(self.rouletteWheel, self.currentTable)
        player = Martingale(self.currentTable)
        currentSim = Simulator(player, game)
