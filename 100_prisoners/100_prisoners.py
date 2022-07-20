# Given N prisoners who may open floor(N/2) boxes, how high can we get their all-find-numbers percentage?
# Written exclusively above 1.0 BAC

# A room with 100 boxes
# Each box has a unique number in it
# A hundred prisoners have 50 guesses each to find their own number inside a box
# If every prisoner finds their number, they win
# If a single prisoner doesn't find their number, everybody dies
#
# Who makes these puzzles?
# I don't know, but Carlo solves them.

import math
import random

_debug = False

_config_prisoner_count	= 100
_config_game_runs	= 10000

def _niave_shuffle_strategy(boxes):
	length = len(boxes)
	random.shuffle(boxes)

class Prisoner:
	def __init__(self, id, game, guess_strategy = None):
		self.id = id

		# Start off knowing nothing
		self.known = []

		# Build up the knowledge containers for this unit
		for x in range(game.prisoner_count):
			self.known.append(None)

		self.last_guess = None
		self.last_value = None

		self.guess_strategy = guess_strategy or Prisoner._niave_guess_strategy
		self.is_safe = False

	@staticmethod
	def _niave_guess_strategy(prisoner, game):
		guess = 0

		# Randomly pick a box that we haven't picked yet
		while prisoner.known[guess] is not None:
			guess = random.randint(0, game.prisoner_count-1)

		return guess

	@staticmethod
	def _dumb_guess_strategy(prisoner, game):
		# Randomly pick a box even if we have used it before
		return random.randint(0, game.prisoner_count-1)

	@staticmethod
	def _circular_guess_strategy(prisoner, game):
		# If there have been no guesses, guess our box number
		if prisoner.last_guess is None:
			return prisoner.id
		# If there have been guesses and we don't know the answer, keep going
		elif not prisoner.known[prisoner.last_value]:
			return prisoner.last_value
		# No good guesses, pick something we haven't guessed before
		return Prisoner._niave_guess_strategy(prisoner, game)

	def make_guess(self, game):
		if _debug:
			print('Prisoner ' + str(self.id) + ' is guessing. Last guess: ' + str(self.last_guess) + ' for ' + str(self.last_value))
		guess = self.guess_strategy(self, game)

		if _debug:
			print('Prisoner guessed ' + str(guess))

		return guess

	def opened(self, box, value):
		self.last_guess = box
		self.last_value = value

		if _debug:
			print('Prisoner ' + str(self.id) + ' guessed ' + str(self.last_guess) + ': ' + str(self.last_value))

		if self.last_value == self.id:
			self.is_safe = True

		self.known[self.last_guess] = self.last_value
		if _debug:
			print('Prisoner now knows: ' + str(self.known))

class Puzzle:
	def __init__(self, length = 100, shuffle_strategy = None):
		self.length = length
		self.shuffle_strategy = shuffle_strategy or _niave_shuffle_strategy

		self.boxes = []
		self._init_boxes(self.length)
		if _debug:
			print('Game boxes: ' + str(self.boxes))

	def _init_boxes(self, game):
		self.boxes = []

		for x in range(self.length):
			self.boxes.append(x)

		self.shuffle_strategy(self.boxes)

class Game:
	def __init__(self, prisoner_count = 100, strategy = None):
		self.prisoner_count = prisoner_count

		self.puzzle = Puzzle(length=prisoner_count, shuffle_strategy=strategy)

	def run(self, prisoner_guess_strategy = None):
		for x in range(self.prisoner_count):
			if _debug:
				print('Running Prisoner ' + str(x))

			prisoner = Prisoner(x, self, prisoner_guess_strategy)
			box_checks = math.floor(self.prisoner_count/2)

			if _debug:
				print('Running Prisoner ' + str(prisoner.id))

			for y in range(box_checks):
				prisoner_guess = prisoner.make_guess(self)
				prisoner.opened(prisoner_guess, self.puzzle.boxes[prisoner_guess])

			if not prisoner.is_safe:
				return x + 1 # 0 is a win, this is the prisoner who killed everyone
			else:
				#print('Prisoner ' + str(x) + ' lived')
				pass

		return 0

if __name__ == "__main__":
	prisoner_count = _config_prisoner_count
	game_runs = _config_game_runs

	# Build the runs
	runs = [
		('dumb', Prisoner._dumb_guess_strategy, []),
		('niave', None, []),
		('circular', Prisoner._circular_guess_strategy, []),
	]

	# Init win lists
	for r in runs:
		for x in range(prisoner_count + 1):
			r[2].append(0)

	# Games
	for r in runs:
		print('Building strategy: ' + r[0] + ' (runs=' + str(game_runs) + ')')

		for x in range(game_runs):
			g1 = Game(prisoner_count)
			r[2][g1.run(r[1])] += 1

	print ('')
	
	# Winners
	for r in runs:
		print('Strategy: ' + r[0])
		print('---')

		print('Winners: ' + str(r[2][0]) + ' (' + str(r[2][0]/game_runs*100) + '%)')

		for x in range(1, prisoner_count):
			if (r[2][x]):
				print('Lost on Prisoner ' + str(x) + ': ' + str(r[2][x]))

		print()

	print('Done!')

