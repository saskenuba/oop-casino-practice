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
        self.streetBets()
        self.dozenBets()
        self.columnBets()
        self.splitbets()
        self.cornerBets()
        self.outsideBets()

    def straightBets(self):
        """Straight bets are simple, one for each number, 1 to 36"""
        for i in range(1, 37):
            newOutcome = Outcome('Number {}'.format(i), 35)
            self.wheel.addOutcome(i, newOutcome)
        zeroStraight = Outcome('0', 35)
        self.wheel.addOutcome(0, zeroStraight)
        zerozeroStraight = Outcome('00', 35)
        self.wheel.addOutcome(37, zerozeroStraight)

    def lineBets(self):
        """ 11 combinations. Counting each row, except for the last one."""
        for i in range(0, 10):
            n = (3 * i) + 1
            newOutcome = Outcome('Line {}-{}-{}-{}-{}-{}'.format(
                n, n + 1, n + 2, n + 3, n + 4, n + 5), 5)
            for j in range(0, 6):
                self.wheel.addOutcome(n + j, newOutcome)

    def streetBets(self):
        """ Each number is a member of one of the twelve street bets."""
        for i in range(0, 12):
            n = (3 * i) + 1
            newOutcome = Outcome('Street {}-{}-{}'.format(n, n + 1, n + 2), 11)
            for j in range(0, 3):
                self.wheel.addOutcome(n + j, newOutcome)

    def dozenBets(self):
        """ Create a bet on each dozen."""
        for i in range(0, 3):
            n = (12 * i) + 1
            newOutcome = Outcome(
                'Dozen {}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}-{}'.format(
                    n, n + 1, n + 2, n + 3, n + 4, n + 5, n + 6, n + 7, n + 8,
                    n + 9, n + 10, n + 11), 2)
            for j in range(0, 12):
                self.wheel.addOutcome(n + j, newOutcome)

    def columnBets(self):
        """ Create three columns, 1-4..34, 2-5..35 and 3-6..36"""
        for i in range(1, 4):
            c = i
            newOutcome = Outcome('Column {}'.format(c, 2), 2)
            for j in range(0, 12):
                self.wheel.addOutcome(c + 3 * j, newOutcome)

    def splitbets(self):
        """Simple bet on two adjacent numbers. It can be either on a row, or a column """
        for i in range(3):
            column = i + 1
            for j in range(12):
                row = j
                currentBin = (3 * row) + column
                """On last column, dont assign split bets to the right"""
                if column != 3:
                    newOutcome = Outcome('Split {}-{}'.format(
                        currentBin, currentBin + 1), 17)
                    self.wheel.addOutcome(currentBin, newOutcome)
                    self.wheel.addOutcome(currentBin + 1, newOutcome)
                """On last row, dont assign split bets downwards"""
                if currentBin < 34:
                    newOutcome = Outcome('Split {}-{}'.format(
                        currentBin, currentBin + 3), 17)
                    self.wheel.addOutcome(currentBin, newOutcome)
                    self.wheel.addOutcome(currentBin + 3, newOutcome)

    def cornerBets(self):
        """ Bet on a corner, that means the point where 4 bins meet. """
        for i in range(2):
            column = i + 1
            for j in range(11):
                row = j
                currentBin = (3 * row) + column
                newOutcome = Outcome('Corner {}-{}-{}-{}'.format(
                    currentBin, currentBin + 1, currentBin + 3,
                    currentBin + 4), 8)
                self.wheel.addOutcome(currentBin, newOutcome)
                self.wheel.addOutcome(currentBin + 1, newOutcome)
                self.wheel.addOutcome(currentBin + 3, newOutcome)
                self.wheel.addOutcome(currentBin + 4, newOutcome)

    def outsideBets(self):
        """ These are all 'outside' bets """
        for i in range(1, 37):
            currentNumber = i

            if currentNumber < 19:
                """Lower Bets"""
                newOutcome = Outcome('Lower Bet', 1)
                self.wheel.addOutcome(currentNumber, newOutcome)
            else:
                """Highter Bets"""
                newOutcome = Outcome('Higher Bet', 1)
                self.wheel.addOutcome(currentNumber, newOutcome)

            if currentNumber % 2 == 0:
                """Even Bet"""
                newOutcome = Outcome('Even Bet', 1)
                self.wheel.addOutcome(currentNumber, newOutcome)
            else:
                """Odd Bet"""
                newOutcome = Outcome('Odd Bet', 1)
                self.wheel.addOutcome(currentNumber, newOutcome)

                """All red bins"""
                RED_BINS = [
                    1, 3, 5, 7, 9, 12, 14, 16, 18, 19, 21, 23, 25, 27, 30, 32,
                    34, 36
                ]

            if currentNumber in RED_BINS:
                """Red Bet"""
                newOutcome = Outcome('Red Bet', 1)
                self.wheel.addOutcome(currentNumber, newOutcome)
            else:
                """Black Bet"""
                newOutcome = Outcome('Black Bet', 1)
                self.wheel.addOutcome(currentNumber, newOutcome)
