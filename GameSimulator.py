#!/usr/bin/python

# TODO how many moves available
class GameSimulator:
	game = 0

	def __init__(self, game):
		self.game = game

	# simulate game and returns who has winning strategy with conf array whats the strategy
	# conf is configuration of game (how the field looks like and who is on turn for instance)
	# depth is for recursion, if depth=0, returns -1
	# return values are
	#	0, [conf]	if player on turn wins
	#	1, [conf]	if other player wins
	#	-1, None	if it doesnt know who wins
	def simulate(self, conf, depth):
		if(depth <= 0):
			return (-1, [])


		# eval win_count (who wins how many times in recursion) and conf_array (strategy)
		win_count = {'-1': 0, '0': 0, '1': 0}
		conf_array = []
		conf_array_nobody_wins = []
		move_index = 0
		while True:
			# do move and break if no more move available
			conf2 = self.game.do_move(conf, move_index)
			if(conf2 == None):
				break
			else: move_index += 1

			# self.game.print_conf(conf2)

			# if winning move, set it to ret
			is_winner = self.game.just_wins(conf2)
			if(is_winner):
				win_count['0'] += 1
				conf_array = [conf2]

			# else recursion and set who wins
			else:
				(winner, conf_array) = self.simulate(conf2, depth - 1)
				conf_array += [conf2]
				if(winner == 1):
					win_count['0'] += 1
				elif(winner == 0):
					win_count['1'] += 1
				else:
					win_count['-1'] += 1
					conf_array_nobody_wins = conf_array

			# break if found 0 winning strategy
			if(win_count['0'] > 0): break

		# return who wins
		if(win_count['0'] > 0):
			return (0, conf_array)
		elif(win_count['-1'] == 0 and win_count['1'] > 0): # if player 1 wins in every circumastances he wins
			return (1, conf_array)
		else:
			return (-1, conf_array_nobody_wins)