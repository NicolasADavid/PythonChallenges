# from ..Misc.bst import BinarySearchTree

def findLevelLinkedList(root):
    level = 0
    result = {}

    q = []
    q.append(root)

    result[level] = q

    while(True):
        q = []

        for i in range(len(result[level])):
            n = result[level][i]
            if n:
                if n.left: q.append(n.left)
                if n.right: q.append(n.right)
            
        if len(q) > 0:
            result[level+1] = q
        else:
            break

        level+=1

    return result

if __name__ == "__main__":
    bst = BinarySearchTree()
    bst.insert(10)
    bst.insert(5)
    bst.insert(6)
    bst.insert(3)
    bst.insert(2)
    bst.insert(4)
    bst.insert(15)
    bst.insert(11)
    bst.insert(16)


    r = findLevelLinkedList(bst.root)

    print(r)

    for key in r:
        print(r[key], key)