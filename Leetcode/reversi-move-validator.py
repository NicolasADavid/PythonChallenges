'''
Reversi (https://en.wikipedia.org/wiki/Reversi), also called Othello, is a game where each disc has two sides, black and white, and after being placed, further moves cause other discs to flip colors. Specifically, a line of discs of one color gets flipped when surrounded on both ends by discs of the opposite color.

In this problem, you're given a 2-dimensional array representing the board. Each position will contain a value of “B” for black, “W” for white, or “*” to represent an empty spot. Additionally, we get a position that is currently empty.

Our task: If it's black's turn to play, our task is to determine if this is a legal move.

A move must meet all of the following criteria:
1. It must have at least one adjacent piece of the opposite color. (Diagonals count)
2. At the far end of a straight line series of opposite color pieces, there must be another matching color piece. 

A simple, 1-dimensional example consider:

* W W W B * * * 

In this case, only the first position is a valid move for black to play because it would surround three white tiles with a black piece at the other end. The remaining positions are invalid moves because they would not surround any white tiles.

Similarly, the sixth position would be a valid move for white because it would surround a single black piece.

This is the starting state of the game with black's possible opening moves labeled with an L:

  0 1 2 3 4 5 6 7
0 * * * * * * * *
1 * * * * * * * *
2 * * * * L * * *
3 * * * B W L * *
4 * * L W B * * *
5 * * * L * * * *
6 * * * * * * * *
7 * * * * * * * *

The board will always be no more than an 8x8 matrix of these three symbols.
 

EXAMPLE(S)
isLegalMove(
  [
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', 'B', 'W', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
  ],
  2, 3)
Output:  true

isLegalMove(
  [
    ['*', 'B', '*', '*', '*'],
    ['*', '*', 'W', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
  ],
  2, 3)
Output:  true

isLegalMove(
  [
    ['*', '*', '*', '*', '*'],
    ['*', '*', 'W', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', 'W', '*', '*'],
    ['*', 'W', '*', '*', '*'],
  ],
  2, 3)
Output:  false
 

FUNCTION SIGNATURE
function isLegalMove(board, r, c)
'''

# from itertools import combinations, permutations, combinations_with_replacement

def isLegalMove(board, r, c):

    if not board or not board[0]:
        return False

    n = len(board)
    m = len(board[0])

    a = [-1,0,1]
    directions = [(i,j) for i in a for j in a]
    directions.remove((0,0))

    # Go in every direction (verticals, horizontals, diagonals)
    for (dr, dc) in directions:

        nr = r
        nc = c

        numOpposite = 0

        while True:

            # Next row
            nr += dr
            # Next col
            nc += dc

            # Validate bounds, end if invalid
            if nr < 0 or nr >= n or nc < 0 or nc >= m:
                break

            next = board[nr][nc]

            # Collect if opposite
            if next == "W":
                numOpposite += 1

            # True if same found
            if next == "B":
                if numOpposite:
                    return True
                else:
                    break
            
            if next == "*":
                break
        
    return False


assert isLegalMove(
  [
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', 'B', 'W', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
  ],
  2, 3) == True

assert isLegalMove(
  [
    ['*', 'B', '*', '*', '*'],
    ['*', '*', 'W', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', '*', '*', '*'],
  ],
  2, 3) == True

assert isLegalMove(
  [
    ['*', '*', '*', '*', '*'],
    ['*', '*', 'W', '*', '*'],
    ['*', '*', '*', '*', '*'],
    ['*', '*', 'W', '*', '*'],
    ['*', 'W', '*', '*', '*'],
  ],
  2, 3) == False