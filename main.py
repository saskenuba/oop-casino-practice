from binbuilder import BinBuilder
from classes import Wheel, Table
from player import Martingale
from roulette import RouletteGame
from simulator import Simulator
from utility import NonRandom
from contextlib import suppress
from exceptions import InvalidBet, PlayerError

notSoRandom = NonRandom()
notSoRandom.setSeed(3)

rouletteWheel = Wheel()
BinBuilder(rouletteWheel)

rouletteTable = Table()
rouletteTable.Table(rouletteWheel)

rouletteGame = RouletteGame(rouletteWheel, rouletteTable)

rouletteSimulation = Simulator(Martingale(rouletteTable), rouletteGame)

# TODO: proper output gather to stdout
with suppress(PlayerError, InvalidBet):
    (maxima, duration) = rouletteSimulation.gather()
    zipped = zip(maxima, duration)
    print(list(zipped))
    print(max(maxima))
