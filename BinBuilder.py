from classes import Outcome


class BinBuilder:
    "Generates all possibles outcomes on every bin"

    def __init__(self, wheel):
        "docstring"
        self.wheel = wheel
        self.buildBins()

    def buildBins(self):
        self.straightBets()
        self.lineBets()

    def straightBets(self):
        """ Straight bets are simple, one for each number, 1 to 36 \
        """
        for i in range(1, 37):
            newOutcome = Outcome('Number {}'.format(i), 35)
            self.wheel.addOutcome(i, newOutcome)
        zeroStraight = Outcome('0', 35)
        self.wheel.addOutcome(0, zeroStraight)
        zerozeroStraight = Outcome('00', 35)
        self.wheel.addOutcome(37, zerozeroStraight)

    def lineBets(self):
        """ 11 combinations. Counting each row, except for the last one. \
        """
        for i in range(0, 10):
            n = (3 * i) + 1
            newOutcome = Outcome('Line {}-{}-{}-{}-{}-{}'.format(
                n, n + 1, n + 2, n + 3, n + 4, n + 5), 5)
            for j in range(0, 6):
                self.wheel.addOutcome(n + j, newOutcome)
