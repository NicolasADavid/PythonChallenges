'''
Go is an ancient game played on a board of 19x19 grid of lines. Black and white stones are placed at the intersections of these lines. 

A group of stones of one color is considered a _connected_ if every stone in the group is reachable from every other, traveling horizontally or vertically. 
For example, the following shows a is a single connected white group because we can traverse through all stones without jumps or moving diagonally. 

  0 1 2 3 4 5
0 + + W + + +
1 + + W + + +
2 + + W W + +
3 + + + W W +
4 + + + + + +
5 + + + + + +

A connected group of stones is captured when *all* adjacent points to the group are occupied by stones of the opposite color. Unoccupied intersections adjacent to a group of stones are called _liberties_. While playing the game, players must keep track of their groups and their liberty counts to look for strong moves to play.

The previous example group of white stones has 10 liberties. If the stone at (2, 3) is removed, it would be broken into two groups. The vertical group of three has 7 liberties, and the horizontal group of two has 6:

  0 1 2 3 4 5
0 + + W + + +
1 + + W + + +
2 + + W + + +
3 + + + W W +
4 + + + + + +
5 + + + + + +

Given a 19x19 board and an occupied position on the board, count the liberties of that connected group. Assume that the board is square and, at most 19x19, the size of a real Go board.
 

EXAMPLE(S)
countLiberties(
  [
    ['+', '+', '+'],
    ['+', 'W', '+'],
    ['+', '+', '+'],
  ],
  1, 1) == 4

countLiberties(
  [
    ['+', '3', '4'],
    ['2', 'B', 'B'],
    ['+', '1', 'B'],
  ],
  1, 1) == 4

Similar to the last example, but the new stone isn't connected.
countLiberties(
  [
    ['B', '+', '+'],
    ['+', 'B', 'B'],
    ['+', '+', 'B'],
  ],
  1, 1) == 4

countLiberties(
  [
    ['W', '+', 'W'],
    ['W', 'B', 'B'],
    ['W', 'W', 'B'],
  ],
  1, 1) == 1
 

Edge cases/Assumptions/Observations : 

- the position in the input is going to be an occupied position, even standalone pieces are considered group 

- the board can be completely occupied, meaning no liberties 

- the board will be 19*19 always, with atleast 1 piece

'''

'''
Follow up :
https://leetcode.com/problems/sliding-puzzle/description/

https://deepmind.google/research/breakthroughs/alphago/
'''

"""    
Save initial group marker [B, W]
Initialize a liberty counter (0)
- define helper function (x, y)
  - Check if in bounds, if not exit helper
  - Check if value is [Opposite group (B, W), or "V"], if yes exit helper
  - Check if value is ["+"], if yes, count, mark, exit helper
  - Value is in group [(B, W)], call helper UP, DOWN, LEFT, RIGHT

Call helper with (x, y)

Return liberty count

"""

def countLiberties(board, x, y) -> int:

    n = len(board) # x
    m = len(board[0]) # y

    targetGroupVal = board[x][y]
    oppositeGroupVal = "B" if targetGroupVal == "W" else "W"

    visitedLibertyVal = "V+"
    visitedGroupVal = "VX"
    libertyVal = "+"
    count = 0
    
    def checkBounds(ex, ey) -> bool:
        return not (ex < 0 or ex >= n or ey < 0 or ey >= m)

    def unmark(ex, ey) -> None:

        # Check bounds
        if not checkBounds(ex, ey):
            return

        val = board[ex][ey]
        
        # Unmark liberty
        if val in [visitedLibertyVal]:
            board[ex][ey] = libertyVal
            return

        if val in [visitedGroupVal]:
            # Unmark occupied
            board[ex][ey] = targetGroupVal
            # Continue exploring
            # UP, DOWN, LEFT, RIGHT
            unmark(ex + 0, ey + 1)
            unmark(ex + 0, ey - 1)
            unmark(ex + 1, ey + 0)
            unmark(ex - 1, ey + 0)

        # Found opposite group val

    def helper(ex, ey) -> None:

        nonlocal count

        # Check bounds
        if not checkBounds(ex, ey):
            return
        
        val = board[ex][ey]

        # Check if value means current exploration should terminate with or without count
        if val in [oppositeGroupVal, visitedGroupVal, visitedLibertyVal]:
            return

        if val in ["+"]:
            # Mark visited liberty
            board[ex][ey] = visitedLibertyVal
            count += 1
            return
        
        # Mark visited occupied
        board[ex][ey] = visitedGroupVal

        # Continue exploring
        # UP, DOWN, RIGHT, LEFT
        helper(ex + 0, ey + 1)
        helper(ex + 0, ey - 1)
        helper(ex + 1, ey + 0)
        helper(ex - 1, ey + 0)

    helper(x, y)
    unmark(x, y)

    return count
        


print(countLiberties(
  [
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', 'B', 'B', 'B', 'B', 'B', '+', '+'],
    ['+', '+', 'B', '+', 'B', '+', 'B', '+', '+'],
    ['+', '+', 'B', 'B', 'B', 'B', 'B', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
  ],
  4, 4
), 18)

print(countLiberties(
  [
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '+'],
    ['+', 'W', 'B', 'B', 'B', 'B', 'B', 'W', '+'],
    ['+', 'W', 'B', '+', 'B', '+', 'B', 'W', '+'],
    ['+', 'W', 'B', 'B', 'B', 'B', 'B', 'W', '+'],
    ['+', 'W', 'W', 'W', 'W', 'W', 'W', 'W', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
  ],
  4, 4
), 2)

print(countLiberties(
  [
    ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
    ['+', '+', '+', 'W', 'B', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['W', 'W', 'W', '+', 'B', '+', '+', '+', '+'],
    ['B', 'B', '+', 'B', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
  ],
  3, 2
), 5)

print(countLiberties(
  [
    ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
    ['+', '+', '+', 'W', 'B', '+', '+', '+', '+'],
    ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
    ['W', 'W', 'W', '+', 'B', '+', '+', '+', '+'],
    ['B', 'B', '+', 'B', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
  ],
  3, 2
), 5)

print(countLiberties(
  [
    ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
    ['+', '+', '+', 'W', 'B', '+', '+', '+', '+'],
    ['+', '+', '+', 'W', '+', '+', '+', '+', '+'],
    ['W', 'W', 'W', 'W', 'B', '+', '+', '+', '+'],
    ['B', 'B', '+', 'B', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
    ['+', '+', '+', '+', '+', '+', '+', '+', '+'],
  ],
  3, 2
), 8)