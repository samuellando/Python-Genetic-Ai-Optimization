# Python Genetic AI Optimization
## What is this?
The survivalOfTheFittest.py script employes an evolutionary approach to the training of Artificial Intelligence based on custom test beds. Given an arbitrary number of iterations, the genetic algorithm randomly generates and crosses over existing AIs in order to obtain an optimized form.
## How it works?
Given an initial random sample of AIs represented by a string of binary numbers, they are tested on a specific testbed which will return an associated score of each AI. The generation is then sorted, a certain bottom percentage is deleted and the top percentage is crossed using a random crossover approach similar to real life. Then the remaining space in the generation is filled with randomly generated AIs and the process is repeated until a satisfactory result is obtained.
## Results
Only one test has been made for this algorithm and can be found as pathFinder.py . This is just an AI that has been trained to move towards a point. and is more of a proof of concept for this algorithm. My next step would be to create a test bed in order to obtain an AI that can play the snake game
### Requirements
- Pygame is required to see the animation on the result.
