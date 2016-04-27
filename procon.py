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
    return edgeSet
        
def finalizeOptTransitions(edgeList, NZ, SDT, JUMP, CUT, F, BETA):
    return 

def addNonoptActions(edges, MA, SDA, DEL, MOVE, PERT):
    return
