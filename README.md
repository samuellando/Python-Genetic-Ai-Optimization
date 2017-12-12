Note that this algorythm and code was originally created with no academeic programing experience, while the algorythm may not be up to standard, it is a proof of concept.

# Python Genetic AI Optimization
## What is this?
The survivalOfTheFittest.py script employes a evolutionary approach to training of Artificial Intelegentce based on custom test beds. Given a aribritary number of iterations, the genetic representation of the Artificial Intelligence will approach an optimal form.
## How it works?
Given a intial random sample of AIs reprisented by a binnary number string, they are tested on a specific testbed witch will return a associated cost of each AI. The generation is then sorted, the bottom precentage are deleted and the top precentage are mated using a random crossover aproach. The remaining space in the generation is filled with randomly generated AIs and the process is repeated untill a satisfactory result is observed.
## Results
Only one test has been made for this algorythm and can be found as pathFinder.py . This is just an AI that has been trained to move towards a point.
** Note you will need pyGame to see any visualizations**
## TODO
1. Comment and clean up algorithm.
2. Create snake game testbed.
3. Create snake game result.
