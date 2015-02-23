#!/usr/bin/env python
from game import Game

NUM_DOORS = 3
NUM_ITERATIONS = 10000

class Experiment:
	def __init__(self, num_iterations, num_doors):
		self.num_doors = num_doors
		self.num_iterations = num_iterations
		self.num_wins_stay = 0
		self.num_wins_switch = 0

	def run_experiment(self):
		for i in range(self.num_iterations):
			current_game = Game(self.num_doors)
			(is_not_switching_win, is_switching_win) = current_game.run_game()
			if not(is_not_switching_win) and not(is_switching_win):
				current_game.print_state()
				raise Exception("error running iteration: " + str(i))				
			self.num_wins_stay += int(is_not_switching_win)
			self.num_wins_switch += int(is_switching_win)
		return (self.num_wins_stay, self.num_wins_switch)

def main():
	experiment = Experiment(NUM_ITERATIONS, NUM_DOORS)
	print experiment.run_experiment()

if __name__ == '__main__':
	main()