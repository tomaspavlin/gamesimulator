#!/usr/bin/python
import sys
import copy

class Game:
	@staticmethod
	def _is_quarto(items):
		for item in items:
			if(item == None): return False

		for i in range(4):
			# if i-bit are equals, return True
			if(sum(map(lambda item: (item & (1 << i)) >> i, items)) % 4 == 0):
				return True

		return False

	@staticmethod
	def _get_empty_fields(table):
		ret = []
		for i in range(4):
			for ii in range(4):
				if(table[i][ii] == None):
					ret += [(i,ii)]

		return ret

	@staticmethod
	def _get_unplaced_items(table):
		ret = range(16)
		for row in table:
			for item in row:
				if(item in ret):
					ret.remove(item)

		return ret

	@staticmethod
	def _item_to_str(item):
		ret = ""

		for i in range(4):
			# if i-bit are equals, return True
			if((item & (1 << i)) >> i == 1):
				ret = "1" + ret
			else:
				ret = "0" + ret

		return ret


	@staticmethod
	def do_move(conf, move_index):
		conf = copy.deepcopy(conf)
		# get empty fields
		empty_fields = Game._get_empty_fields(conf['table'])

		# get unplaced_items
		unplaced_items = Game._get_unplaced_items(conf['table'])
		unplaced_items.remove(conf['chosen_item'])

		# do move
		if(move_index >= len(empty_fields)*len(unplaced_items)): return None

		i1 = move_index / len(unplaced_items)
		i2 = move_index % len(unplaced_items)

		(i, ii) = empty_fields[i1]
		conf['table'][i][ii] = conf['chosen_item']
		conf['chosen_item'] = unplaced_items[i2]

		return conf

	@staticmethod
	def just_wins(conf):
		table = conf['table']

		for i in range(4):
			if(Game._is_quarto([table[0+i][0],table[0+i][1],table[0+i][2],table[0+i][3]])): return True
			if(Game._is_quarto([table[0][0+i],table[1][0+i],table[2][0+i],table[3][0+i]])): return True

		for i in range(3):
			for ii in range(3):
				if(Game._is_quarto([table[0+i][0+ii],table[0+i][1+ii],table[1+i][0+ii],table[1+i][1+ii]])): return True
		
		if(Game._is_quarto([table[0][0],table[1][1],table[2][2],table[3][3]])): return True
		if(Game._is_quarto([table[3][0],table[2][1],table[1][2],table[0][3]])): return True

		return False

	@staticmethod
	def print_conf(conf):
		for row in conf['table']:
			for item in row:
				if(item == None):
					sys.stdout.write(".\t")
				else:
					sys.stdout.write(Game._item_to_str(item) + "\t")

			print ""
		print "Chosed " + Game._item_to_str(conf['chosen_item'])
		print "\n"