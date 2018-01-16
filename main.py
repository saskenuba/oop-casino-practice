from binbuilder import BinBuilder
from classes import Wheel, Table
from player import Martingale, Passenger57
from roulette import RouletteGame
from simulator import Simulator
import simulator
import roulette

rouletteWheel = Wheel()
BinBuilder(rouletteWheel)

rouletteTable = Table()
rouletteTable.Table(rouletteWheel)

rouletteGame = RouletteGame(rouletteWheel, rouletteTable)

rouletteSimulation = Simulator(Martingale(rouletteTable), rouletteGame)

# TODO: proper output gather to stdout
print(rouletteSimulation.gather())
