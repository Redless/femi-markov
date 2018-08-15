import pickle
import numpy as np
from random import random

class Node:
    '''class representing a node in a Markov Chain'''

    def __init__(self, label=None):
        '''creates a new node'''
        if label:
            self.label = label
        self.departures = 0
        self.jumps={}
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
        self.departures += 1
        if destination not in self.jumps.keys():
            self.jumps[destination]=1
        else:
            self.jumps[destination]+=1

    def getDepartureProb(self,destination):
        '''gets probablity of a given jump'''
        if destination in self.jumps:
            return float(self.jumps[destination])/float(self.departures)
        else:
            return 0

    def getJump(self):
        '''returns where the jump is to, based on jump probabilities'''
        randresult = random()
        tot = 0
        for i in self.jumps:
            tot += self.getDepartureProb(i)
            if tot > randresult:
                return i

class FixedNode:
    '''class representing a node with a fixed transition probabilities.
    use this node if you already know what you want all of your transition
    probabilities to be'''

    def __init__(self,label):
        self.label = label
        return None

    def addWeights(self, jumps, weights):
        self.jumps = {}
        for i in range(len(jumps)):
            self.jumps[jumps[i]] = weights[i]

    def addDeparture(self,destination):
        pass

    def getDepartureProb(self,destination):
        return self.jumps[destination]

    def getJump(self):
        '''returns where the jump is to, based on jump probabilities'''
        randresult = random()
        tot = 0
        for i in self.jumps:
            tot += self.getDepartureProb(i)
            if tot > randresult:
                return i


class MarkovChain:
    '''class respresenting a Markov Chain'''

    def __init__(self,sourcefile=None):
        '''creates a new markov chain'''
        if not sourcefile:
            self.nodes = {}
            self.currNodeOn = None
        else:
            with open(sourcefile,"rb") as fileIn:
                self = pickle.load(fileIn)

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
        self.nodes[origin].addDeparture(self.nodes[destination])

    def printTransitionProbs(self):
        for nodeLabel in self.nodes:
            originNode=self.nodes[nodeLabel]
            for i in self.nodes:
                print('Transition prob from '+str(nodeLabel)+' to '+str(i)+': '+str(originNode.getDepartureProb(self.nodes[i])))

    def saveChainPickle(self,destfilename):
        '''uses pickle to save the markov chain to a file'''
        with open(destfilename,"wb") as destfile:
            pickle.dump(self,destfile)

    def saveChainCSV(self,destfilename):
        '''saves markov chain to a CSV file'''
        tempStr=''
        with open(destfilename,'w') as destfile:
            for originNodeLabel in self.nodes:
                originNode=self.nodes[originNodeLabel]
                for otherNode in originNode.jumps:
                    tempStr+=str(originNodeLabel)+','+str(otherNode)+','+str(originNode.jumps[otherNode])+'\n'
            destfile.write(tempStr)

    def getTransitionMatrix(self):
        nodeKeys=list(self.nodes)
        matrix=[]
        for i in nodeKeys:
            row=[]
            for j in nodeKeys:
                row.append(self.nodes[j].getDepartureProb(self.nodes[i]))
            matrix.append(row)
        return matrix,nodeKeys

    def printTransitionMatrix(self):
        matrix=self.getTransitionMatrix()[0]
        for i in range(len(matrix)):
            tempStr=''
            for j in range(len(matrix[i])):
                tempStr+=str(matrix[i][j])
                tempStr+='\t'
            print(tempStr)

    def setCurrNodeOn(self,destlabel):
        '''moves the current node to a specific node'''
        self.currNodeOn = self.nodes[destlabel]

    def simulateJump(self):
        '''simulates a transition from the current node based on probabilities'''
        self.currNodeOn = self.currNodeOn.getJump()
        return self.currNodeOn

    def simulateManyJumps(self,n,start,batches):
        '''simulates many transitions'''
        outstring = ''
        for i in range(batches):
            self.setCurrNodeOn(start)
            for j in range(n):
                outstring += str(self.currNodeOn.label)
                self.simulateJump()
                outstring += ' -> '
            outstring += str(self.currNodeOn.label)
            outstring += '\n'
        return outstring

def addCSVFile(filename):
    '''Creates a MarkovChain object based on an external CSV file'''
    chain=MarkovChain()
    with open(filename,'r') as source:
        lines=source.readlines()
        for i in range(len(lines)):
            lines[i]=lines[i].rstrip('\n')
            lines[i]=lines[i].split(',')
            for j in range(int(lines[i][2])):
                chain.addMovement(lines[i][0],lines[i][1])
    return chain

def addPickleFile(filename):
    '''Creates a MarkovChain object based on a previously generated pickle file'''
    with open(filename,'rb') as openfile:
        chain=pickle.load(openfile)
    return chain

def addMatrix(matrix):
    '''creates a markovchain from a matrix'''
    outChain = MarkovChain()
    for i in range(len(matrix)):
        outChain.nodes[i] = FixedNode(i)
    for i in range(len(matrix)):
        outChain.nodes[i].addWeights([outChain.nodes[j] for j in outChain.nodes],[matrix[j][i] for j in range(len(matrix))])
    return outChain
