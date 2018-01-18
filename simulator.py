from exceptions import InvalidBet, PlayerError


class Simulator():
    def __init__(self, player, game):
        """Returns statistics of the chosen casino game with a given
        player/betting strategy.

        It reports raw statistics on a number of sessions of play.

        initDuration (int): default number of sessions per game.
        samples (int): number of game cycles per session.
        initStake (int): default player stake.

        game (obj Game): game to simulate.
        player (obj Player): player betting strategy to simulate.

        """
        self.initDuration = 250
        self.samples = 50
        self.initStake = 1000
        self.player = player
        self.game = game

    def session(self):
        """Run a single session of the game, and returns all
        the ending stakes of each cycle. """
        self.setUpSession()
        stakeList = list()

        try:
            while True:
                self.game.cycle(self.player, 0)
                stakeList.append(self.player.stake)
        except (PlayerError, InvalidBet) as e:
            return stakeList

    def gather(self):
        """Executes the number of session indicated by samples parameter

        Returns a tuple with the session maximum stakes, and the number of
        rounds."""
        durations = list()
        maxima = list()
        minima = list()

        for _ in range(self.initDuration):
            sessionStakes = self.session()
            durations.append(len(sessionStakes))
            maxima.append(max(sessionStakes))
            minima.append(min(sessionStakes))

        return (maxima, minima, durations)

    def setUpSession(self):
        """Do the initial setup for the session to start."""
        self.player.stake = self.initStake
        self.player.roundsToGo = self.samples
        self.player.reset()
