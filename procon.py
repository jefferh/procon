from __future__ import division
import time
import random
import numpy as np
from collections import deque

# See Archibald, T. W., K. I. M. McKinnon, and L. C. Thomas. "On the generation of Markov decision processes." Journal of the Operational Research Society (1995): 354-361.

def generateOptTransitions(m, LEN, CYC):
    # Generate the transition structure for the optimal policy.
    # m = number of states
    # LEN = length of each random walk
    # CYC = number of previous states to exclude when generating each random walk

    X = range(m) # list of all the states
    visitedStates = set([]) # set containing the states visited on the current random walk
    CYCstates = deque([]) # queue containing last CYC states visited in the current random walk
    edgeSet = set([]) # set of tuples representing the edges in the generated transition graph

    # Generate initial random walk of length LEN
    print "--------------------"
    print "Initial random walk:"
    print "--------------------"
    x0 = random.choice(X) # initial state
    print x0
    visitedStates.add(x0)
    CYCstates.append(x0)
    for t in range(LEN):
        if t < LEN-1:
            x1 = random.choice(list(set(X) - set(CYCstates)))
        else:
            x1 = random.choice(list(visitedStates - set(CYCstates)))
        print x1
        visitedStates.add(x1)
        CYCstates.append(x1)
        if len(CYCstates) > CYC:
            CYCstates.popleft()
        edgeSet.add((x0,x1))
        x0 = x1
    print "--------------------"
    print "Initial edge set:"
    print "--------------------"
    print edgeSet
    print "--------------------"
    print "Initial set of visited states:"
    print "--------------------"
    print visitedStates
    print "--------------------"

    # Connect the isolated states to the generated random walk
    CYCstates = deque([]) # re-initialize CYCstates
    while len(set(X) - visitedStates): # while there's a state that hasn't been visited
        x0 = random.choice(list(set(X) - visitedStates))
        print x0
        visitedStates.add(x0)
        CYCstates.append(x0)
        x1 = random.choice(list(set(X) - set(CYCstates)))
        print x1
        while not x1 in visitedStates:
            visitedStates.add(x1)
            CYCstates.append(x1)
            if len(CYCstates) > CYC:
                CYCstates.popleft()
            edgeSet.add((x0,x1))
            x0 = x1            
            x1 = random.choice(list(set(X) - set(CYCstates)))
        edgeSet.add((x0,x1))
    print edgeSet
    print visitedStates
    # return edgeSet
    
    # Assign weights to the edges
    edgeWeightSet = {}
    for edge in edgeSet:
        edgeWeightSet[edge] = np.random.uniform()
    print edgeWeightSet
    # return edgeWeightSet

    # Normalize the weights to get transition probabilities
    eWgrouped = [] # the i-th element will be a dict containing the edges incident to vertex i
    for i in range(m): 
      eWgrouped.append({k:edgeWeightSet[k] for k in edgeWeightSet.keys() if k[0]==i})
    # return eWgrouped
    eWnormed = []
    for i in range(len(eWgrouped)):
        vertexSum = sum(eWgrouped[i].values())
        for key in eWgrouped[i]:
            eWnormed.append(eWgrouped[i][key]/vertexSum)
    return eWnormed
        
def finalizeOptTransitions(edgeList, NZ, SDT, JUMP, CUT, F, BETA):
    return 

def addNonoptActions(edges, MA, SDA, DEL, MOVE, PERT):
    return
