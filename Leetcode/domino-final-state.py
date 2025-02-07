'''
You're given an array containing either '.', 'L', or 'R' values. These values represent a starting state of a row of dominoes. L means the domino has been pushed to the left. R means the domino has been pushed to the right. All elements to the left  of an L get pushed to the left and all elements to the right of an R get pushed to the right. If a domino is pushed in both directions simultaneously, it stays up.

Given the starting state array, return the updated array representing the final state of the dominos. All dominos should be L, R or . if it stays standing upright.
 

EXAMPLE(S)
[., L, ., R, .] -> [L, L, ., R, R]
[., R, ., ., L, .] -> [., R, R, L, L, .]
[., R, ., ., ., L, .] -> [., R, R, .,  L, L, .]
[., R, ., L, ., L, ., R, .] -> [., R, ., L, L, L, ., R,R]
 
QUESTIONS:
- allowed to modify the input
- 1 <= len(dominosRow)

[., R, ., ., ., ., L, .]
[., R, R, ., ., L, L, .]

[., R, R, R, L, L, L, .]
[., R, R, R, L, L, L, .] DONE!
*/
'''

from collections import deque

def finalDominosState(dominosRow):

    falling = []

    # Collect every R and L in the input
    for idx, domino in enumerate(dominosRow):
        if domino in ["R", "L"]:
            falling.append(idx)

    # Iterate through falling look at the index and push left or right
    # popleft from queue process that index (push left or right)
    # append index of the domino
    while falling:

        toFall = []

        for idx in falling:
        
            if dominosRow[idx] == "R":
                # if the next idx is not OOB and if the next dom is upright
                if idx + 1 < len(dominosRow) and dominosRow[idx + 1] == ".":
                    # case 1: next is out of bounds (we have a fall!)
                    if idx + 2 >= len(dominosRow):
                        toFall.append(((idx + 1), "R"))
                    # case 2: next is same direction or upright (we have a fall!)
                    elif dominosRow[idx + 2] == "R" or dominosRow[idx + 2] == ".":
                        toFall.append(((idx + 1), "R"))
                    # case 3: next is the opposite direction (no fall) 


            if dominosRow[idx] == "L":
                # if the next idx is not OOB and if the next dom is upright
                if idx - 1 >= 0 and dominosRow[idx - 1] == ".":
                    # case 1: next is out of bounds (we have a fall!)
                    if idx - 2 < 0:
                        toFall.append(((idx - 1), "L"))
                    # case 2: next is same direction or upright (we have a fall!)
                    elif dominosRow[idx - 2] == "L" or dominosRow[idx - 2] == ".":
                        toFall.append(((idx - 1), "L"))
                    # case 3: next is the opposite direction (no fall) 

        # Update the dominos that fell
        # toFall: [(idx, direction)..]
        for fall in toFall:
            dominosRow[fall[0]] = fall[1] 

        # Update the falling queue
        falling = deque([fall[0] for fall in toFall])


        
    return dominosRow

print(finalDominosState([".", "L", ".", "R", "."])) # -> [L, L, ., R, R]
print(finalDominosState([".", "R", ".", ".", "L", "."])) # -> [., R, R, L, L, .]
print(finalDominosState([".", "R", ".", ".", ".", "L", "."])) # -> [., R, R, .,  L, L, .]
print(finalDominosState([".", "R", ".", "L", ".", "L", ".", "R", "."])) # -> [., R, ., L, L, L, ., R,R]
print(finalDominosState(["R", ".", ".", ".", ".", ".", ".", "."])) # -> ['R', 'R', 'R', 'R', 'R', 'R', 'R', 'R']
print(finalDominosState(["L", ".", ".", ".", ".", ".", ".", "."])) # -> ['L', '.', '.', '.', '.', '.', '.', '.']
print(finalDominosState([".", ".", ".", ".", ".", ".", ".", "R"])) # -> ['.', '.', '.', '.', '.', '.', '.', 'R']
print(finalDominosState([".", ".", ".", ".", ".", ".", ".", "L"])) # -> ['L', 'L', 'L', 'L', 'L', 'L', 'L', 'L']


