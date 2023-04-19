from typing import List, Set, Tuple


class Solution:

    def threeSum(self, nums: List[int]) -> List[List[int]]:

        threeSolsSet, dupes = set(), set()

        def twoSum(target) -> Set[Tuple[int, int]]:

            twoSolsSet = set()

            numMap = {}

            for idx, num in enumerate(nums):

                # if(numMap[target - num]):
                if(numMap.setdefault(target - num, None)):
                    twoSolsSet.add((num, nums[numMap[target-num]]))

                numMap[num] = idx

            return twoSolsSet

        for idx, num in enumerate(nums):

            if(num not in dupes):

                tuplesForThreeSols = twoSum(-num)

                for (a, b) in tuplesForThreeSols:

                    theNums = [num, a, b]
                    theNumsSorted = sorted(theNums)
                    threeSolsSet.add(tuple(theNumsSorted))

                dupes.add(num)


        return threeSolsSet

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right



#dict
# testDict = {}
# testDict.setdefault(1, None) #get value associated with key 1, None if it doesn't exist

#set
# testSet = set()

# if (1 not in testSet):
#     print("no 1 in set")

# testSet.add(2)

#array

#enumeration

#binary tree

#math
# quotient, remainder = divmod(8, 3) # q = 2, r = 1

#DFS

#BFS

#List

# a = list("12345")
# while a:
#     a.pop() # pops from end: 5, 4, 3, ...

#Tuples

if __name__ == "__main__":
    print("GRIND LC")
    # a = list("12345")

    # while a:
    #     print(a)
    #     v = int(a.pop())

    #     print("v: ", v)
    #     print("a: ", a)

