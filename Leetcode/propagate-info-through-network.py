#
'''
Propagate information through a network

A subset of database servers in a grid network received an update that they must replicate to the remaining nodes. 
Each second, Nodes broadcast updates to their immediate neighbors, north, west, south, and east.

Given an initial state of the nodes with the updated information, 
determine how many seconds it will take to propagate the update to the entire network.
 

EXAMPLE(S)
If the state of the network at the 0th second is:
[
  [0, 0, 0],
  [0, 1, 0],
  [0, 0, 0]
]
Then it takes 2 seconds to propagate the information. After the 1st second:
[
  [0, 1, 0],
  [1, 1, 1],
  [0, 1, 0]
]
After the 2nd second:
[
  [1, 1, 1],
  [1, 1, 1],
  [1, 1, 1]
]
 

FUNCTION SIGNATURE
function broadcastTime(network) {
def broadcastTime(network: list[list[int]]) -> int:
'''
from typing import List
def broadcastTime(network: List[List[int]]):

    if not network:
        return 0
    
    nextIter = []
    currIter = []

    # coordinate/node = Tuple(row, column)
    
    # Collect nodes for first iteration
    for m in range(len(network)):
        
        for n in range(len(network[0])):
            
            if network[m][n]:
                nextIter.append((m,n))
    
    m = len(network)
    n = len(network[0])

    time = 0

    while nextIter:
        currIter = list(nextIter)
        nextIter.clear()

        while currIter:
            
            node = currIter.pop()

            # Visit neighbors
            dirs = [(0, 1), (1, 0), (0, -1), (-1, 0)]

            for dir in dirs:
                #visit neighbor

                nr = node[0] + dir[0]
                nc = node[1] + dir[1]

                # check valid
                if nr >= 0 and nr < m and nc >= 0 and nc < n:
                    # check value
                    if not network[nr][nc]:
                        # if valid and not value, flip and add to nextIter
                        network[nr][nc] = 1
                        nextIter.append((nr, nc))
        
        if nextIter:
            time += 1
    
    return time

print(broadcastTime([[0, 0, 0], [0, 1, 0], [0, 0, 0]]))
                        