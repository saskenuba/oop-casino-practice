from classes import Bet
from exceptions import InvalidBet


class Player():
    def __init__(self, table):
        "The player superclass"
        self.stake = 200
        self.roundsToGo = 30
        self.table = table
        self.initialBet = 5
        self.nextBet = self.initialBet

    def win(self, bet):
        """Method to credit stake to player"""
        amountWon = bet.winAmount()
        self.stake += amountWon
        print('You won {} by betting {}.'.format(amountWon, bet))

    def lose(self, bet):
        """Method to debit stake from player"""
        amountLost = bet.loseAmount()
        self.stake -= amountLost
        print('You lost {} by betting {}.'.format(bet.loseAmount(), bet))

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


class Passenger57(Player):
    def __init__(self, table):
        "A very persistent player, whose whole purpose is to bet on blacks"
        super().__init__(table)
        self.favoriteBet = table.currentWheel.getOutcome('Black Bet')

    def placeBets(self):
        """Updates the table he is playing with bets."""
        self.nextBet = self.initialBet

        if not self.isPlaying():
            raise InvalidBet("Player has left the table.")

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

        if not self.isPlaying():
            raise InvalidBet("Player has left the table.")

        self.playerNewBet = Bet(self.nextBet, self.favoriteBet)
        self.table.placeBet(self.playerNewBet)

    def win(self, bet):
        """Reset loss count and bet multiple"""
        super().win(bet)
        self.lossCount = 0
        self.betMultiple = 1

    def lose(self, bet):
        """Updates also loss count"""
        super().lose(bet)
        self.lossCount += 1
        self.betMultiple *= 2
