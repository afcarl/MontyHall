##About this repo:
a simulation of the Monthy Hall problem, in Python. Maybe I should name this repository to MontyPython. 

##Problem definition:
You are on a game show and have to choose one among three doors. Behind one is a new car and behind the other two are goats (caution: this game only works if you'd rather have a car over a goat). The host knows which door has the car. After you choose you door, the host opens one of the two remaining doors, revealing a goat. Now you have two options: stay with your initial choice or switch and choose the other door. Which option offers a higher probability of picking the door with the car? 

##To run the code:
```
src/experiment.py
```
To edit the experiment parameters you can run -
```
src/experiment.py -i <NUM_ITERATIONS> -d <NUM_DOORS>
```

For example -
```
src/experiment.py -i 1000 -d 4
```

Both parameters are optional and default to 10000 iterations and 3 doors.

##Results (for simulation with 3 doors):
![alt tag](https://github.com/nihit/MontyHall/blob/master/results/plot.png)

##Useful references: 
* Wikipedia entry: http://en.wikipedia.org/wiki/Monty_Hall_problem.
* Discussion on Quora: https://www.quora.com/Why-does-the-Monty-Hall-problem-seem-counter-intuitive
* Article about Marilyn vos Savant: http://priceonomics.com/the-time-everyone-corrected-the-worlds-smartest/

