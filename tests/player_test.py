import unittest
from classes import Outcome, Bin, Wheel, Bet, Table
from roulette import RouletteGame
from player import Passenger57, Martingale, SevenReds
from binbuilder import BinBuilder
from exceptions import InvalidBet, PlayerError
from utility import NonRandom

# TODO: test apropriately 7 losses, doubling after each loss, and then bet on blacks.
# TODO: Continue on the statistics section

class test_Game(unittest.TestCase):
    def setUp(self):
        # creating wheel with nonrandom value
        notSoRandom = NonRandom()
        notSoRandom.setSeed(33)

        self.rouletteWheel = Wheel(notSoRandom)
        BinBuilder(self.rouletteWheel)

        self.currentTable = Table()
        self.currentTable.Table(self.rouletteWheel)
        self.currentTable.betMinimum = 5
        self.game = RouletteGame(self.rouletteWheel, self.currentTable)

    def tearDown(self):
        del self.game

    def test_Player_Passenger57(self):
        playerPassenger = Passenger57(self.currentTable)
        playerPassenger.initialBet = 5
        expectedStake = [205, 210, 215, 210, 205, 200, 205]

        for i in range(6):
            self.game.cycle(playerPassenger, 0)
            self.assertEqual(playerPassenger.stake, expectedStake[i])

    def test_Player_Martingale(self):
        playerMartingale = Martingale(self.currentTable)
        playerMartingale.initialBet = 5
        expectedStake = [205, 210, 215, 210, 200, 180, 220]
        """Expect Player to left the game because lack of funds."""
        for i in range(6):
            self.game.cycle(playerMartingale, 0)
            self.assertEqual(playerMartingale.stake, expectedStake[i])

    def test_Player_SevenReds(self):
        playerSevenReds = SevenReds(self.currentTable)
        self.currentTable.betLimit = 1000
        for i in range(50):
            self.game.cycle(playerSevenReds, 0)
