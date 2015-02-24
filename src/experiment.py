#!/usr/bin/env python
import argparse

from game import Game

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

def main(num_iterations, num_doors):
	experiment = Experiment(num_iterations, num_doors)
	print experiment.run_experiment()

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description="Run a Monty Hall experiment.")
	parser.add_argument("-i", action="store", dest="num_iterations", default=10000,
		type=int, help="The number of iterations. Default is 10000.")
	parser.add_argument("-d", action="store", dest="num_doors", default=3,
		type=int, help="The number of doors. Default is 3.")
	args = parser.parse_args()
	main(args.num_iterations, args.num_doors)