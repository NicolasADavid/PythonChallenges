#!/bin/python3

import math
import os
import random
import re
import sys

# Complete the viralAdvertising function below.
# def viralAdvertising(n):

#     initialPeople = 5
#     peopleSharedWith = 3

#     def helper(peopleIn, daysLeft, sum):

#         if daysLeft == 0:
#             return sum


#         peopleToAdd = math.floor(peopleIn/2)
#         sum += peopleToAdd

#         return helper(peopleToAdd*peopleSharedWith, daysLeft - 1, sum)

#     return helper(initialPeople, n, 0)

def viralAdvertising(n):

    shared = 5
    totalOpened = 0

    for _ in range(0, n):
        opened = math.floor(shared/2)
        totalOpened += opened
        shared = opened*3

    return totalOpened


if __name__ == '__main__':

    print(viralAdvertising(3)) #9
    print(viralAdvertising(4)) #15