# Python Genetic AI Optimization
## What is this?
The survivalOfTheFittest.py script employes a evolutionary approach to training of Artificial Intelegentce based on custom test beds. Given a aribritary number of iterations, the genetic algorythm randomly generates and crosses over exitsing AIs in order to obtain an optimized form.
## How it works?
Given a intial random sample of AIs reprisented by a string of binary numbers, they are tested on a specific testbed witch will return a associated score of each AI. The generation is then sorted, a certain bottom precentage are deleted and the top precentage are crossed using a random crossover aproach similar to real life. Then the remaining space in the generation is filled with randomly generated AIs and the process is repeated untill a satisfactory result is obtained.
## Results
Only one test has been made for this algorythm and can be found as pathFinder.py . This is just an AI that has been trained to move towards a point. and is more of a proof of concept for this algorythm. My next step would be to create a test bed in order to obtain an AI that can play the snake game
### Requirements
- Pygame is required to see the anymation on the result.
