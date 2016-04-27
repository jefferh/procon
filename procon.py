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

    X = set(range(m)) # state set
    qVisited = deque([]) # queue containing last CYC states visited in the current random walk
    edges = [] # list of tuples representing the edges in the generated transition graph

    
    

def finalizeOptTransitions(edges, NZ, SDT, JUMP, CUT, F, BETA):

def addNonoptActions(edges, MA, SDA, DEL, MOVE, PERT):
