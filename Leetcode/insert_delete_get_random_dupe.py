from collections import defaultdict
from random import choice
# from typing import List

class RandomizedCollection(object):

    def __init__(self):
        self.d = defaultdict(list)
        self.arr = []
        

    def insert(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.d:
            r = False
        else:
            r = True

        self.arr.append(val)
        self.d[val].append(len(self.arr) - 1)

        return r

    def remove(self, val):
        """
        :type val: int
        :rtype: bool
        """

        if val in self.d:

            idx = self.d[val][-1]
            last_val = self.arr[-1]

            # Swap the last element with the element to be removed
            self.arr[idx] = last_val
            self.d[last_val].remove(len(self.arr) - 1)
            self.d[last_val].append(idx)

            self.arr.pop()
            self.d[val].pop()

            if not self.d[val]:
                del self.d[val]

            return True
            
        return False
        
        

    def getRandom(self):
        """
        :rtype: int
        """
        return choice(self.arr)
    
# if __name__ == "__main__":
    # # Example usage
    # obj = RandomizedCollection()
    # print(obj.insert(1))  # True
    # print(obj.insert(1))  # False
    # print(obj.insert(2))  # True
    # print(obj.getRandom())  # Randomly returns either 1 or 2
    # print(obj.remove(1))  # True
    # print(obj.getRandom())  # Randomly returns either 1 or 2

    # a = ["RandomizedCollection","insert","insert","insert","insert","insert","remove","remove","remove","insert","remove","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom","getRandom"]
    # b = [[],[1],[1],[2],[2],[2],[1],[1],[2],[1],[2],[],[],[],[],[],[],[],[],[],[]]

    # for func, ar in zip(a,b):
    #     if func == "RandomizedCollection":
    #         obj = RandomizedCollection()
    #     elif func == "insert":
    #         print(obj.insert(*ar))
    #     elif func == "remove":
    #         print(obj.remove(*ar))
    #     elif func == "getRandom":
    #         print(obj.getRandom())
    #     else:
    #         raise ValueError(f"Unknown function: {func}")