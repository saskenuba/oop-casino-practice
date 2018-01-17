from exceptions import PlayerError, InvalidBet


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

    def cycle(self, player, debug=None):
        """Executes a single cycle of play with a given player.

        First of all, it wil check if the player is indeed still playing.
        Next will place the player bets and deduct one round of the
        player overall.

        Then the roullete will run and chose a winning bin.

        After, it will pick the iterator on the table, so it can check
        the active outcomes whose has bets on it.
        """

        try:
            player.placeBets()
            player.roundOneLess()
        except (PlayerError, InvalidBet) as e:
            raise

        winningBin = self.wheel.next()
        activeBets = [x.outcome for x in self.table.__iter__()]

        if winningBin is None:
            # There has to be an outcome
            return

        if debug:
            print()
            print('There are {} rounds left.'.format(player.roundsToGo))
            print('Active bets on table {}'.format(next(iter(activeBets))))
            print('Player budget before roll: {}'.format(player.stake))
            print('Winning bin is {}'.format(next(iter(winningBin.outcomes))))

        roundSummary = {'winningBin': winningBin, 'activeBets': activeBets}

        player.setWinners(winningBin.outcomes)

        for oc in activeBets:
            if oc in winningBin.outcomes:
                player.win(player.playerNewBet)
            else:
                player.lose(player.playerNewBet)

        if debug:
            print('Player budget after roll: {}'.format(player.stake))
            print()

        self.table.clearAllBets()

        return roundSummary
