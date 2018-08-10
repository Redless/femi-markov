import pickle
import numpy as np

class Node:
    '''class representing a node in a Markov Chain'''

    def __init__(self, label = None):
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

class MarkovChain:
    '''class respresenting a Markov Chain'''

    def __init__(self,sourcefile=None):
        '''creates a new markov chain'''
        if not sourcefile:
            self.nodes = {}
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
        self.nodes[origin].addDeparture(destination)
    def printTransitionProbs(self):
        for nodeLabel in self.nodes:
            originNode=self.nodes[nodeLabel]
            for i in originNode.jumps:
                print('Transition prob from '+str(nodeLabel)+' to '+str(i)+': '+str(originNode.jumps[i]/originNode.departures))
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
            tempStr=''
    def getTransitionMatrix(self):
        nodes=list(self.nodes.keys())
        matrix=[]
        for i in range(len(nodes)):
            origin=self.nodes[nodes[i]]
            row=[]
            for j in range(len(nodes)):
                jumpKeys=list(origin.jumps.keys())
                if nodes[j] in jumpKeys:
                    row.append(origin.jumps[nodes[j]]/origin.departures)
                else:
                    row.append(0)
            matrix.append(row)
        return matrix,nodes
    def printTransitionMatrix(self):
        matrix=self.getTransitionMatrix()[0]
        for i in range(len(matrix)):
            tempStr=''
            for j in range(len(matrix[i])):
                tempStr+=str(matrix[i][j])
                tempStr+='\t'
            print(tempStr)
    def getSteadyState(self): #little broken? don't know if fully works
        matrix,nodes=self.getTransitionMatrix()
        zeroes=[]
        try:
            w,v=np.linalg.eig(np.array(matrix))
            for i in range(len(w)):
                if w[i]==1:
                    x=v[:,i]
                    total=sum(x)
                    break
            for i in range(len(nodes)):
                x[i]/=total
                print(str(nodes[i]+': '+str(x[i])))
        except np.linalg.LinAlgError as err:
            print(err)
            print('No steady-state probabilities')


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
