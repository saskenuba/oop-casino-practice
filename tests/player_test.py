import unittest
from classes import Wheel, Table
from roulette import RouletteGame
from player import Passenger57, Martingale, SevenReds, PlayerRandom, Player1326
from player import Player1326ZeroWins, Player1326OneWins, Player1326TwoWins
from player import Player1326ThreeWins
from binbuilder import BinBuilder
from exceptions import InvalidBet, PlayerError
from utility import NonRandom

# TODO: Continue on the statistics section


class test_Game(unittest.TestCase):
    def setUp(self):
        # creating wheel with nonrandom value
        self.notSoRandom = NonRandom()
        self.notSoRandom.setSeed(33)

        self.rouletteWheel = Wheel(self.notSoRandom)
        BinBuilder(self.rouletteWheel)

        self.currentTable = Table()
        self.currentTable.Table(self.rouletteWheel)
        self.currentTable.betMinimum = 5
        self.game = RouletteGame(self.rouletteWheel, self.currentTable)

    def tearDown(self):
        del self.game
        del self.notSoRandom

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
        self.notSoRandom.setCustomSequence(
            [32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 32, 33])
        for i in range(17):
            if i == 8:
                self.assertEqual(playerSevenReds.stake, 190)
            if i == 16:
                self.assertEqual(playerSevenReds.stake, 210)
            self.game.cycle(playerSevenReds, 0)

    def test_Player_PlayerRandom(self):
        playerRandom = PlayerRandom(self.currentTable, self.notSoRandom)
        self.game.cycle(playerRandom, 0)
        self.assertIn(playerRandom.favoriteBet,
                      self.rouletteWheel.getBin(self.notSoRandom.value))

    def test_Player_Player1326(self):
        player1326 = Player1326(self.currentTable)
        self.notSoRandom.setCustomSequence(
            [33, 33, 33, 33, 32, 33, 33, 33, 32, 33, 33, 32, 33, 32])
        expectedStake = [
            210, 240, 260, 320, 310, 320, 350, 370, 310, 320, 350, 330, 340,
            310
        ]

        for roll in range(14):
            self.game.cycle(player1326, 0)
            if roll == 3:
                # win whole strategy
                self.assertIsInstance(player1326.state, Player1326ZeroWins)
                self.assertEqual(player1326.stake, expectedStake[roll])
            elif roll == 7:
                # got three wins
                self.assertIsInstance(player1326.state, Player1326ThreeWins)
                self.assertEqual(player1326.stake, expectedStake[roll])
            elif roll == 10:
                # got two wins
                self.assertIsInstance(player1326.state, Player1326TwoWins)
                self.assertEqual(player1326.stake, expectedStake[roll])
            elif roll == 12:
                # got one win
                self.assertIsInstance(player1326.state, Player1326OneWins)
                self.assertEqual(player1326.stake, expectedStake[roll])
            elif roll == 13:
                # got no wins
                self.assertIsInstance(player1326.state, Player1326ZeroWins)
                self.assertEqual(player1326.stake, expectedStake[roll])
