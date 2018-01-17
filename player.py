from classes import Bet
from exceptions import InvalidBet, PlayerError


class Player():
    def __init__(self, table):
        "The player superclass"
        self.stake = 200
        self.roundsToGo = 30
        self.table = table
        self.initialBet = 10
        self.nextBet = self.initialBet

    def win(self, bet):
        """Method to credit stake to player"""
        amountWon = bet.winAmount()
        self.stake += amountWon

    def lose(self, bet):
        """Method to debit stake from player"""
        amountLost = bet.loseAmount()
        self.stake -= amountLost

    def isPlaying(self):
        """Returns player current status.

        For a player to be playing, it needs to have budget left, and rounds.
        """
        return (self.stake >= self.nextBet) and self.roundsToGo != 0

    def stakeResetToDefault(self):
        """Resets stake back to the default value."""
        self.stake = 200

    def roundOneLess(self):
        """Take one round out of the player."""
        self.roundsToGo -= 1

    def reset(args):
        """Reset player to initial settings"""
        pass


class Passenger57(Player):
    def __init__(self, table):
        "A very persistent player, whose whole purpose is to bet on blacks"
        super().__init__(table)
        self.favoriteBet = table.currentWheel.getOutcome('Black Bet')

    def placeBets(self):
        """Updates the table he is playing with bets."""
        self.nextBet = self.initialBet

        # there was an except here, out of budget
        if not self.isPlaying():
            return 0

        self.playerNewBet = Bet(self.nextBet, self.favoriteBet)
        self.table.placeBet(self.playerNewBet)


class Martingale(Player):
    def __init__(self, table):
        "A player the exponentially doubles the bet on every loss"
        super().__init__(table)
        self.favoriteBet = table.currentWheel.getOutcome('Black Bet')
        self.lossCount = 0
        self.betMultiple = 1

    def placeBets(self):
        """Updates the table he is playing with bets."""
        self.nextBet = self.initialBet * self.betMultiple

        # there was an except here, out of budget
        if not self.isPlaying():
            raise PlayerError('No budget left to meet table minimum.')

        self.playerNewBet = Bet(self.nextBet, self.favoriteBet)

        try:
            self.table.placeBet(self.playerNewBet)
        except (InvalidBet) as error:
            raise InvalidBet('Bet over table limit.')

    def win(self, bet):
        """Reset loss count and bet multiple"""
        super().win(bet)
        self.lossCount = 0
        self.betMultiple = 1

    def reset(self):
        """Hard reset player to initial settings"""
        super().reset()
        self.betMultiple = 1
        self.lossCount = 0

    def lose(self, bet):
        """Updates also loss count"""
        super().lose(bet)
        self.lossCount += 1
        self.betMultiple *= 2
