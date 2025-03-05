#!/bin/python3

import math
import os
import random
import re
import sys


#
# Complete the 'getMinConnectionCost' function below.
#
# The function is expected to return a LONG_INTEGER_ARRAY.
# The function accepts following parameters:
#  1. INTEGER_ARRAY warehouseCapacity
#  2. 2D_INTEGER_ARRAY additionalHubs
#
def getMinConnectionCost(warehouseCapacity, queries):

    n = len(warehouseCapacity)

    runningTotal = [0] * n

    for i in range(n):
        if i == 0:
            runningTotal[i] = warehouseCapacity[n-1] - warehouseCapacity[i]
        else:
            runningTotal[i] = runningTotal[i-1] + warehouseCapacity[n-1] - warehouseCapacity[i]

    ans = []

    total = runningTotal[n-1]

    for query in queries:

        firstHubIdx, secondHubIdx = query[0] - 1, query[1] - 1

        # Saved cost of this hub
        hubCost1 = warehouseCapacity[n-1] - warehouseCapacity[firstHubIdx]

        # Cost savings of all hubs before this hub
        hub1Savings = 0
        if firstHubIdx > 0:
            hub1Savings += firstHubIdx*hubCost1
            
        savings1 = hubCost1 + hub1Savings

        # Saved cost of this hub
        hubCost2 = warehouseCapacity[n-1] - warehouseCapacity[secondHubIdx]

        # Cost savings of all hubs between first and second hub
        hub2Savings = 0
        if secondHubIdx - firstHubIdx > 1:
            hub2Savings += (secondHubIdx - firstHubIdx - 1) * hubCost2
        
        savings2 = hubCost2 + hub2Savings 

        newCost = total - savings1 - savings2

        ans.append(newCost)

    return ans


# def getMinConnectionCost_worse(warehouseCapacity, queries):
    
#     ans = []
#     n = len(warehouseCapacity)
    
#     cache = {}
    
#     print(f"warehouseCapacity: {warehouseCapacity}")
#     print(f"queries: {queries}")
    
#     for query in queries:
        
#         cacheKey = "".join([str(x) for x in query])
#         if cacheKey in cache:
#             ans.append(cache[cacheKey])
#             continue
        
#         cost = 0
        
#         # Prepare hubs
#         firstHubIdx, secondHubIdx = query[0] - 1, query[1] - 1
#         hubs = [firstHubIdx, secondHubIdx]
#         if n not in hubs:
#             hubs.append(n-1)
        
#         # For every warehouse capacity
#         for idx, capacity in enumerate(warehouseCapacity):
            
#             # Hubs don't count
#             if idx == hubs[0]:
#                 hubs.pop(0)
#                 continue
            
#             minCost = warehouseCapacity[hubs[0]] - capacity
#             cost += minCost
        
#         ans.append(cost)
#         cache[cacheKey] = cost
    
#     return ans
            
            
if __name__ == '__main__':
    hubs1 = [1, 2, 3, 4, 5, 6, 7, 8, 9] 
    queries1 = [[4, 7]]
    print(getMinConnectionCost(hubs1, queries1)) # 10

    hubs2 = [3, 6, 10, 15, 20]
    queries2 = [[2, 4]]
    print(getMinConnectionCost(hubs2, queries2)) # 8


    
            
# if __name__ == '__main__':
#     fptr = open(os.environ['OUTPUT_PATH'], 'w')

#     warehouseCapacity_count = int(input().strip())

#     warehouseCapacity = []

#     for _ in range(warehouseCapacity_count):
#         warehouseCapacity_item = int(input().strip())
#         warehouseCapacity.append(warehouseCapacity_item)

#     additionalHubs_rows = int(input().strip())
#     additionalHubs_columns = int(input().strip())

#     additionalHubs = []

#     for _ in range(additionalHubs_rows):
#         additionalHubs.append(list(map(int, input().rstrip().split())))

#     result = getMinConnectionCost(warehouseCapacity, additionalHubs)

#     fptr.write('\n'.join(map(str, result)))
#     fptr.write('\n')

#     fptr.close()
