from classes import Bet


class Passenger57():
    def __init__(self, table):
        "A very persistent player, whose whole purpose is to bet on blacks"
        self.table = table
        self.favoriteBet = 'Black Bet'

    def placeBets(self):
        """Updates the table he is playing with bets."""
        playerNewBet = Bet(5, self.favoriteBet)
        self.table.placeBet(playerNewBet)

        # TODO: win a lose methods
