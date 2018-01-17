from classes import Bet
from exceptions import InvalidBet, PlayerError


class Player():
    """The player superclass. Each specialization is a different betting strategy
    used by the simulation to gather statistics.


    win(bet:obj): add winning to player stake
    winners: all the winning outcomes from the wheel
    lose(bet:obj): subtract lose to player stake
    isPlaying: return bool based if player still has funds to place a bet
    stakeResetToDefault: resets player stake back to default
    roundOneLess: take out one round from overall
    """

    def __init__(self, table):
        "The player superclass"
        self.stake = 200
        self.roundsToGo = 30
        self.table = table
        self.initialBet = 10
        self.nextBet = self.initialBet
        self.winners = list()

    def win(self, bet):
        """Method to credit stake to player"""
        amountWon = bet.winAmount()
        self.stake += amountWon

    def lose(self, bet):
        """Method to debit stake from player"""
        amountLost = bet.loseAmount()
        self.stake -= amountLost

    def setWinners(self, outcomes):
        self.winners = outcomes

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

    def placeBets(self):
        """Updates the table he is playing with bets.

        This should be extended by subclasses with the desired
        next bet strategy.

        """

        if not self.isPlaying():
            raise PlayerError('No budget left to meet table minimum.')

        self.playerNewBet = Bet(self.nextBet, self.favoriteBet)

        try:
            self.table.placeBet(self.playerNewBet)
        except (InvalidBet) as error:
            raise InvalidBet('Bet over table limit.')


class Passenger57(Player):
    def __init__(self, table):
        "A very persistent player, whose whole purpose is to bet on blacks"
        super().__init__(table)
        self.favoriteBet = table.currentWheel.getOutcome('Black Bet')

    def placeBets(self):
        """Updates the table he is playing with bets."""
        self.nextBet = self.initialBet
        super().placeBets()


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
        super().placeBets()

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


class SevenReds(Martingale):
    def __init__(self, table):
        """A player that waits for seven straight reds before betting
        on blacks."""
        super().__init__(table)
        self.redCount = 7

    def setWinners(self, outcomes):
        """If there is a red winner, subtract one from redcount,
        else resets it."""
        super().setWinners(outcomes)

        if self.favoriteBet not in self.winners:
            print(self.redCount)
            self.redCount -= 1
        else:
            self.redCount = 7

    def placeBets(self):
        """Only bets after seven reds"""
        if self.redCount == 0:
            print('apostei')
            super().placeBets()
        return

    def win(self, bet):
        super().win(bet)
        self.redCount = 7

    def lose(self, bet):
        super().lose(bet)
        self.redCount = 7
