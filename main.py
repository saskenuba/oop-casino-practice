from binbuilder import BinBuilder
from classes import Wheel, Table
from player import Martingale, SevenReds, Passenger57, PlayerRandom
from roulette import RouletteGame
from simulator import Simulator
from utility import NonRandom
from contextlib import suppress
from exceptions import InvalidBet, PlayerError
from statistics import IntegerStatistics as stats

notSoRandom = NonRandom()
notSoRandom.setSeed(4)

rouletteWheel = Wheel()
BinBuilder(rouletteWheel)

rouletteTable = Table()
rouletteTable.Table(rouletteWheel)

rouletteGame = RouletteGame(rouletteWheel, rouletteTable)

rouletteSimulation = Simulator(PlayerRandom(rouletteTable), rouletteGame)

(maxima, minima, duration) = rouletteSimulation.gather()
zipped = zip(maxima, minima, duration)
print('{:>7} {:>4} {:>4} {:>3}'.format('Session', 'Max', 'Min', 'Dur'))
for i, (a, b, c) in enumerate(zipped):
    print('{:>7} {:>4} {:>4} {:>2}'.format(i+1, a, b, c))

print('Mean of maximum values: {}'.format(stats.mean(maxima)))
print('Standard deviation of maximum: {}'.format(stats.stdev(maxima)))
print('Mean of minima values: {}'.format(stats.mean(minima)))
print('Standard deviation of minima: {}'.format(stats.stdev(minima)))
print('Mean of duration: {}'.format(stats.mean(duration)))
print('Standard deviation of duration: {}'.format(stats.stdev(duration)))
