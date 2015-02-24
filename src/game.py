from door import Door
from random import randint

class Game:
	def __init__(self, num_doors):
		self.num_doors = num_doors
		self.doors = []

	# both inclusuve: a <= random <= b
	def __get_random_index(self, a, b):
		return randint(a,b)

	def __initialize_doors(self, car_door_index):
		for i in range(self.num_doors):
			currentDoor = Door((i == car_door_index), False, False)
			self.doors.append(currentDoor)

	def __open_relevant_doors(self, doors_not_to_open):
		for i in range(self.num_doors):
			self.doors[i].is_revealed = i not in doors_not_to_open

	def __is_win(self, index_a, index_b):
		return index_a == index_b

	def run_game(self):
		#step 1: decide door for the car
		car_door_index = self.__get_random_index(0, self.num_doors - 1)
		self.__initialize_doors(car_door_index)
		
		#step2: contenstant chooses a door at random
		chosen_door_index = self.__get_random_index(0, self.num_doors - 1)
		self.doors[chosen_door_index].is_chosen = True

		#step3: host opens all doors except two: door with the car and the door chosen by contestant
		doors_not_to_open = set()
		doors_not_to_open.add(car_door_index)
		doors_not_to_open.add(chosen_door_index)	
		additional_door_not_to_open = -1
		#but in case both are the same, randomly selected another door which will not be opened	
		if car_door_index == chosen_door_index:
			while True:
				additional_door_not_to_open = self.__get_random_index(0, self.num_doors - 1)
				#hack: "door chosen at random" might actually be the same as door with car. In that case repeat
				if (additional_door_not_to_open != car_door_index):
					break
			doors_not_to_open.add(additional_door_not_to_open)
		self.__open_relevant_doors(doors_not_to_open)

		#step 4: winning !
		stay_option = chosen_door_index
		if additional_door_not_to_open >= 0:
			switch_option = additional_door_not_to_open
		else:
			switch_option = car_door_index

		return (self.__is_win(car_door_index, stay_option), self.__is_win(car_door_index, switch_option))

	def print_state(self):
		print "num_doors: " + str(self.num_doors)
		for i in range(self.num_doors):
			header = "Door[" + str(i) + "]:" + " "
			is_car = "is_car: " + str(self.doors[i].is_car) + " "
			is_chosen = "is_chosen: " + str(self.doors[i].is_chosen) + " "
			is_opened = "is_opened:  " + str(self.doors[i].is_revealed)
			print header + is_car + is_chosen + is_opened
		return
