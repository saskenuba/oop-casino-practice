class RouletteGame():
    def __init__(self, wheel, table):
        """This class manages the sequences of actions that defines
        the game of Roulette.

        Including notifying the player to place bets, spinning the wheel
        and resolving the bets present on the table.

        The Game class does not include the Player at the constructor, it
        exists independently of any particular player.

        """

        self.wheel = wheel
        self.table = table

    def cycle(self, player):
        """Executes a single cycle of play with a given player.

        First it will place the player bets, then the roullete will run
        and chose a winning bin.

        After, it will pick the iterator on the table, so it can check
        the active outcomes whose has bets on it.
        """
        player.placeBets()
        winningBin = self.wheel.next()
        activeBets = [x.outcome for x in self.table.__iter__()]

        print('Winning bin is {}'.format(winningBin))
        print()
        print('Active bets on table {}'.format(activeBets))

        for oc in activeBets:
            if oc in winningBin.outcomes:
                player.win(player.playerNewBet)
            else:
                player.lose(player.playerNewBet)

        return {'winningBin': winningBin, 'activeBets': activeBets}
