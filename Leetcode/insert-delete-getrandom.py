from random import choice

class RandomizedSet:

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.d = {}
        self.arr = []
        
    def insert(self, val: int) -> bool:
        """
        Inserts a value to the set. Returns true if the set did not already contain the specified element.
        """

        # If val is in d, return false
        if val in self.d:
            return False

        # Insert into d with the index val was inserted into arr at
        self.arr.append(val)
        self.d[val] = len(self.arr)-1

        return True

    def remove(self, val: int) -> bool:
        """
        Removes a value from the set. Returns true if the set contained the specified element.
        """

        # If val not in d, return false
        if val not in self.d:
            return False


        # Remove from array and then d
        # Use index of val to swap the last element of arr with val
        valIdx = self.d[val]        
        swapVal = self.arr[-1]

        # Put swapVal into arr[valIdx] to overwrite val
        self.arr[valIdx] = swapVal
        # Update index in d of swapVal
        self.d[swapVal] = valIdx

        # Remove last element of arr and val from d
        self.arr.pop()
        # Remove val from d
        self.d.pop(val)

        return True

    def getRandom(self) -> int:
        """
        Get a random element from the set.
        """
        
        return choice(self.arr)

if __name__ == "__main__":
    
    obj = RandomizedSet()
    param_1 = obj.insert(1)
    param_2 = obj.remove(2)
    param_3 = obj.getRandom()