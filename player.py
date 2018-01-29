from classes import Bet
from functools import partial
from exceptions import InvalidBet, PlayerError
import random


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
        next bet strategy."""

        if not self.isPlaying():
            raise PlayerError('No budget left to meet table minimum.')

        self.playerNewBet = Bet(self.nextBet, self.favoriteBet)

        try:
            self.table.placeBet(self.playerNewBet)
        except (InvalidBet) as error:
            raise InvalidBet('Bet over table limit.')


class PlayerRandom(Player):
    def __init__(self, table, rng=None):
        """Player that make random bets.

        rng (obj:: NonRandom) OPTIONAL arg: if user wants predictable outcome"""
        super().__init__(table)
        self.rng = rng if rng is not None else random.Random()

    def placeBets(self):
        """Chose a random outcome"""
        self.favoriteBet = random.sample(
            self.rng.choice(self.table.currentWheel).outcomes, k=1)[0]
        super().placeBets()


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
            self.redCount -= 1
        else:
            self.redCount = 7

    def placeBets(self):
        """Only bets after seven reds"""
        if self.redCount == 0:
            super().placeBets()
        elif not self.isPlaying():
            raise PlayerError('No budget left to meet table minimum.')
        return

    def win(self, bet):
        super().win(bet)
        self.redCount = 7

    def lose(self, bet):
        super().lose(bet)
        self.redCount = 7


# Applying the state behavior design pattern to Player 1-3-2-6 Class
class Player1326(Player):
    def __init__(self, table):
        """docstring"""
        super().__init__(table)
        self.favoriteBet = self.table.currentWheel.getOutcome('Black Bet')

        # default state
        self.state = Player1326StateFactory.getInstance('zerowins', self)

    def placeBets(self):
        """Updates the table with a bet based on current state"""
        self.state.currentBet()
        super().placeBets()

    def win(self, bet):
        """Extends superclass method to update player stake.
        Use current state to determine what next state will be.
        Delegate decision to state object."""
        super().win(bet)
        self.state.nextWon()

    def lose(self, bet):
        """Overrides superclass method.
        Use current state to determine what next state will be.
        Delegate decision to state object."""
        super().lose(bet)
        self.state.nextLost()


class Player1326State():
    """
    This is the superclass of all Player1326 states.

    currentBet(obj:bet): set the amount to be betted by the current
    state of the bet strategy.

    """

    def __init__(self, player):
        "docstring"
        self.player = player
        self.betMultiplier = int()

    def currentBet(self):
        """Method used to set the amount to be betted.

        This method got refactored from being extended to each class,
        to the superclass."""
        self.player.nextBet = self.player.initialBet * self.betMultiplier

    def nextWon(self):
        """Assign the next state to context on win."""
        self.player.state = self.nextStateWin()

    def nextLost(self):
        """Creates new Player1326State instance to be used when
        bet was loser. This method is the same for every subclass,
        because whenever the player lose the method is the same """
        self.player.state = Player1326StateFactory.getInstance(
            'zerowins', self)


class Player1326StateFactory():
    """This is a factory with lazy instantiation. It saves a reference to the obj
    to avoid repeating obj creationg."""
    _values = dict()

    @classmethod
    def getInstance(cls, name, player):
        if name in cls._values:
            return cls._values[name]

        if name == 'zerowins':
            plr = Player1326ZeroWins(player)
            cls._values['zerowins'] = plr
            return cls._values['zerowins']

        elif name == 'onewins':
            plr = Player1326OneWins(player)
            cls._values['onewins'] = plr
            return cls._values['onewins']

        elif name == 'twowins':
            plr = Player1326TwoWins(player)
            cls._values['twowins'] = plr
            return cls._values['twowins']

        elif name == 'threewins':
            plr = Player1326ThreeWins(player)
            cls._values['threewins'] = plr
            return cls._values['threewins']


# All subclasses of player 1326 state


class Player1326ZeroWins(Player1326State):
    def __init__(self, player):
        "State where player hasnt won any bet"
        super().__init__(player)
        self.betMultiplier = 1
        self.nextStateWin = partial(Player1326StateFactory.getInstance,
                                    'onewins', self.player)


class Player1326OneWins(Player1326State):
    def __init__(self, player):
        "State where player has won one bet"
        super().__init__(player)
        self.betMultiplier = 3
        self.nextStateWin = partial(Player1326StateFactory.getInstance,
                                    'twowins', self.player)


class Player1326TwoWins(Player1326State):
    def __init__(self, player):
        "State where player has won two bet"
        super().__init__(player)
        self.betMultiplier = 2
        self.nextStateWin = partial(Player1326StateFactory.getInstance,
                                    'threewins', self.player)


class Player1326ThreeWins(Player1326State):
    def __init__(self, player):
        "State where player has won three bet"
        super().__init__(player)
        self.betMultiplier = 6
        self.nextStateWin = partial(Player1326StateFactory.getInstance,
                                    'zerowins', self.player)
