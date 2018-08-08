# femi-markov

This code represents a Markov chain by constantly adding transitions between different nodes.
Transition probabilities can then be approximated by keeping track of the various jumps from a certain node to the others.

In addition, pickle and CSV files can be used to store and load in Markov chains.

node.py contains the classes to represent nodes and chains as well as functions to load in chains.
main.py contains a menu to add jumps to a chain as well as display transition probabilities and save/load in chains.
