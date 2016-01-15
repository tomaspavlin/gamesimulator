#!/usr/bin/python

from Quarto import Game
from GameSimulator import GameSimulator

#	black	high	square	hollow

# depth = 3
conf = {
	'table': [
		[0b1010,				None,			None,			None	],
		[None,				0b0110,			0b0100,			None	],
		[None,				0b1001,			0b0101,			None	],
		[0b0111,				0b1000,			None,			0b1011	]
		],
	'chosen_item': 0b0011
}



def sim(depth,conf):
	print "Trying for depth " + str(depth) + "..."

	simulator = GameSimulator(Game)
	winner, conf_arr = simulator.simulate(conf,depth)

	if(winner == 0):
		print "Found winning strategy for FIRST player."
	elif(winner == 1):
		print "Found winning strategy for SECOND player."
	else:
		print "No winning strategy found"
		print ""
		print_strategy(conf_arr)
		return False


	print ""
	print_strategy(conf_arr)

	return True

def print_strategy(conf_arr):
	if(conf_arr != None):
		for conf in reversed(conf_arr):
			Game.print_conf(conf)
			# print ""


depth = 1
while not sim(depth,conf):
	depth += 1