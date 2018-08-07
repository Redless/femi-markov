


class Node:
    '''class representing a node in a Markov Chain'''

    def __init__(self, label = None):
        '''creates a new node'''
        if label:
            self.label = label
        self.departures = 0
        self.edges = []
        self.weights = []
        return None

    def __str__(self):
        '''converts node to string for debugging'''
        outstring = "Node: "
        if self.label:
            outstring+=str(self.label)
        else:
            outstring+=":(unlabeled):"
        return outstring

    def addDeparture(self,destination):
        '''adds a departure to the node'''
        try:
            self.weights[self.edges.index(destination)]+=1
        except ValueError:
            self.weights.append(1)
            self.edges.append(destination)
        self.departures += 1

class MarkovChain:
    '''class respresenting a Markov Chain'''

    def __init__(self):
        '''creates a new markov chain'''
        self.nodes = {}
        return None

    def __str__(self):
        '''converts to string for debugging'''
        for i in self.nodes:
            print(self.nodes[i])

    def addMovement(self,origin,destination):
        '''adds a movement from origin to destination'''
        if not origin in self.nodes:
            self.nodes[origin] = Node(origin)
        if not destination in self.nodes:
            self.nodes[destination] = Node(destination)
        self.nodes[origin].addDeparture(destination)
    def printTransitionProbs(self):
        for nodeLabel in self.nodes:
            originNode=self.nodes[nodeLabel]
            for i in range(len(originNode.edges)):
                print("Transition probability for Node "+str(nodeLabel)+" to Node "+str(originNode.edges[i])+": "+str(originNode.weights[i]/originNode.departures))
