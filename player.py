from classes import Bet


class Passenger57():
    def __init__(self, table, wheel):
        "A very persistent player, whose whole purpose is to bet on blacks"
        # TODO: is it really needed to insert wheel to get outcome?
        self.table = table
        self.favoriteBet = wheel.getOutcome('Black Bet')

    def placeBets(self):
        """Updates the table he is playing with bets."""
        self.playerNewBet = Bet(200, self.favoriteBet)
        self.table.placeBet(self.playerNewBet)

    def win(self, bet):
        print('You won {} by betting {}.'.format(bet.winAmount(), bet))

    def lose(self, bet):
        print('You lost {} by betting {}.'.format(bet.loseAmount(), bet))
