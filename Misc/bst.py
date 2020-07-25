import queue
from typing import List

class Node:
    def __init__(self, val):
        self.val = val
        self.left = None
        self.right = None

class BinarySearchTree:
    def __init__(self):
        self.root = None

    def insert(self, val):

        newNode = Node(val)

        if not self.root:
            self.root = newNode
            return self
        else:
            current = self.root
            while(True):
                if(val == current.val):
                    return None

                if(val < current.val):
                    if(not current.left):
                        current.left = newNode
                        return self
                    else:
                        current = current.left
                elif(val > current.val):
                    if not current.right:
                        current.right = newNode
                        return self
                    else:
                        current = current.right

        return self

    def find(self, val):
        current = self.root
        found = False

        if not self.root: return False

        while((not not current) & (not found)):
            if(val < current.val):
                current = current.left

            elif(val > current.val):
                current = current.right

            else:
                found = True

        if found: return current

        return None

    def BFS(self):

        root = self.root

        if not root: return None

        d = []
        q = queue.Queue()
        q.put(root)

        while(not q.empty()):
            root = q.get()
            d.append(root)
            
            if(root.left):
                q.put(root.left)
                
            if(root.right):
                q.put(root.right)

        return d

    def preOrder(self) -> List[Node]:
        current = self.root
        if not current: return []
        d = []

        def helper(node):
            d.append(node)
            if(node.left): helper(node.left)
            if(node.right): helper(node.right)

        helper(current)
        return d

    def postOrder(self) -> List[Node]:
        current = self.root
        if not current: return []
        d = []

        def helper(node):
            if(node.left): helper(node.left)
            if(node.right): helper(node.right)
            d.append(node)

        helper(current)
        return d
        
    def inOrder(self) -> List[Node]:
        current = self.root
        if not current: return []
        d = []

        def helper(node):
            if(node.left): helper(node.left)
            d.append(node)
            if(node.right): helper(node.right)

        helper(current)
        return d

    def reverseOrder(self) -> List[Node]:
        current = self.root
        if not current: return []
        d = []

        def helper(node):
            if(node.right): helper(node.right)
            d.append(node)
            if(node.left): helper(node.left)

        helper(current)
        return d


if __name__ == "__main__":

    bst = BinarySearchTree()
    bst.insert(2)
    bst.insert(1)
    bst.insert(3)

    def helper(arr):
        if arr:
            for node in arr:
                print(node.val)

        print("----")
                
    helper(bst.BFS())
    helper(bst.preOrder())
    helper(bst.postOrder())
    helper(bst.inOrder())
    helper(bst.reverseOrder())