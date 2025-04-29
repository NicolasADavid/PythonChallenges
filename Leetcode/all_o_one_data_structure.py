"""
432. All O`one Data Structure
Hard
Topics
Companies
Design a data structure to store the strings' count with the ability to return the strings with minimum and maximum counts.

Implement the AllOne class:

AllOne() Initializes the object of the data structure.
inc(String key) Increments the count of the string key by 1. If key does not exist in the data structure, insert it with count 1.
dec(String key) Decrements the count of the string key by 1. If the count of key is 0 after the decrement, remove it from the data structure. It is guaranteed that key exists in the data structure before the decrement.
getMaxKey() Returns one of the keys with the maximal count. If no element exists, return an empty string "".
getMinKey() Returns one of the keys with the minimum count. If no element exists, return an empty string "".
Note that each function must run in O(1) average time complexity.

 

Example 1:

Input
["AllOne", "inc", "inc", "getMaxKey", "getMinKey", "inc", "getMaxKey", "getMinKey"]
[[], ["hello"], ["hello"], [], [], ["leet"], [], []]
Output
[null, null, null, "hello", "hello", null, "hello", "leet"]

Explanation
AllOne allOne = new AllOne();
allOne.inc("hello");
allOne.inc("hello");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "hello"
allOne.inc("leet");
allOne.getMaxKey(); // return "hello"
allOne.getMinKey(); // return "leet"
"""

class Node(object):
    def __init__(self, count):
        self.count = count
        self.keys = set()
        self.prev = None
        self.next = None

class AllOne(object):

    def __init__(self):

        """
        Initialize your data structure here.
        """
        self.keys = {}
        self.first = None
        self.top = Node(float('inf'))
        self.bottom = Node(float('-inf'))

        self.top.prev = self.bottom
        self.bottom.next = self.top
        
    def make_first(self, key):
        first = Node(1)
        first.keys.add(key)

        # new node forward
        first.next = self.bottom.next
        # new node backward
        first.prev = self.bottom

        # if the next node exists, update its previous pointer
        self.bottom.next.prev = first
        self.bottom.next = first

        self.first = first
    
    def remove_first(self):
        self.first = None


    def inc(self, key):
        """
        :type key: str
        :rtype: None
        """

        if key in self.keys:
            # move the key to the next node
            node = self.keys[key]
            
            next_node = node.next

            # if the next node does not exist or the count is not equal to the current node's count + 1
            if not next_node or next_node.count != node.count + 1:
                # create a new node
                next_node = Node(node.count + 1)

                next_node.prev = node
                next_node.next = node.next

                if node.next:
                    node.next.prev = next_node
                node.next = next_node

            # add the key to the next node
            next_node.keys.add(key)
            # remove the key from the current node
            node.keys.remove(key)
            # Update the dictionary
            self.keys[key] = next_node

            # if the current node is empty, remove it
            if not node.keys:
                # remove the current node
                node.prev.next = node.next
                if node.next:
                    node.next.prev = node.prev

                # if the count is 1
                if node.count == 1:
                    self.remove_first()
        else:
            if not self.first:
                self.make_first(key)
            else:
                # add the key to the first node
                self.first.keys.add(key)
                
            # add the key to the dictionary
            self.keys[key] = self.first

    def dec(self, key):
        """
        :type key: str
        :rtype: None
        """

        node = self.keys[key]

        # remove the key from the current node
        node.keys.remove(key)

        if node.count == 1:
            # remove the key from the dictionary
            del self.keys[key]
        else:

            prev_node = node.prev

            if not prev_node or node.prev.count != node.count - 1:
                if node.count == 2:
                    self.make_first(key)
                    prev_node = self.first
                else:
                    # create a new node
                    prev_node = Node(node.count - 1)
                    prev_node.keys.add(key)

                # add the new node to the list
                prev_node.next = node
                prev_node.prev = node.prev

                if node.prev:
                    node.prev.next = prev_node
                node.prev = prev_node

            # add the key to the previous node
            prev_node.keys.add(key)

            # Update the dictionary
            self.keys[key] = prev_node

        # if the current node is empty, remove it
        if not node.keys:
            # remove the current node
            node.prev.next = node.next
            if node.next:
                node.next.prev = node.prev

            # if the count is 1, remove the key from the dictionary
            if node.count == 1:
                    self.remove_first()
                # # remove first node
                # self.bottom.next = self.first.next
                # self.first.next.prev = self.bottom
                # self.first = None


    def getMaxKey(self):
        """
        :rtype: str
        """
        # return self.top.prev.count if self.top.prev else ""
        return next(iter(self.top.prev.keys)) if self.top.prev and len(self.top.prev.keys) else ""
        

    def getMinKey(self):
        """
        :rtype: str
        """
        # return self.bottom.next.count if self.bottom.next else ""
        return next(iter(self.bottom.next.keys)) if self.bottom.next and len(self.bottom.next.keys) else ""
        


# Your AllOne object will be instantiated and called as such:
# obj = AllOne()
# obj.inc(key)
# obj.dec(key)
# param_3 = obj.getMaxKey()
# param_4 = obj.getMinKey()

# Test cases
if __name__ == "__main__":
    # allOne = AllOne()
    # allOne.inc("hello")
    # allOne.inc("hello")
    # print(allOne.getMaxKey())  # return "hello"
    # print(allOne.getMinKey())  # return "hello"
    # allOne.inc("leet")
    # print(allOne.getMaxKey())  # return "hello"
    # print(allOne.getMinKey())  # return "leet"

    # Test case 2
    allOne = AllOne()
    allOne.inc("a")
    allOne.inc("b")
    allOne.inc("b")
    allOne.inc("c")
    allOne.inc("c")
    allOne.inc("c")
    allOne.dec("b")
    allOne.dec("b")
    print(allOne.getMinKey())  # return "a"
    allOne.dec("a")
    print(allOne.getMaxKey())  # return "c"
    print(allOne.getMinKey())  # return "c"