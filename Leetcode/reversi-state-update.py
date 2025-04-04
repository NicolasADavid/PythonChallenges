'''
Reversi (https://en.wikipedia.org/wiki/Reversi), also called Othello, is a game where each piece has two sides, black and white, and after being placed, further moves cause other pieces to flip tiles. Specifically, a line of pieces of one color gets flipped when they become surrounded by pieces of the opposite color on both ends.

In this problem, we will be given a 2-dimensional array representing the board. Each position will contain a value of “B”, “W”, or “*” representing empty. Additionally, we get a position that is currently empty. Update the board to the new state after that play, including any flips if it is black’s turn to play. You can modify the existing array, but either way, return the board (2d array) with the new state.

EXAMPLE(S)
For example, consider the row:

1 2 3 4 5 6 7 8
* B W W W W * *

If black places a piece at position 7, the white pieces in between get flipped, so the result is:

1 2 3 4 5 6 7 8
* B B B B B B *

This can happen on a row, column, or diagonal and even at the same time. In the following example, if white place on position (5, 5), then all of the black pieces flip to white!

  1 2 3 4 5 6 7 8
1 * * * * * * * *
2 * W * * * * * *
3 * * B * * * * *
4 * * * B * * * *
5 W B B B ! * * *
6 * * * * B * * *
7 * * * * B * * *
8 * * * * W * * *
 

FUNCTION SIGNATURE
def reversi(board, x, y):

'''

"""

main function which accepts a 2D matrix representation of a game in progress, a coordinate where someone is playing, and which player
    if there's already a piece at that location, bail out

    helper function which accepts a vector direction and a current coordinate
        if this cell has the opposite color
            set DidCapture to result from calling helper with same vector and next coordinate in that line
            if DidCapture
                set current cell to my own color
            return DidCapture
        otherwise, if the cell has the same color
            return True, to indicate I found a capturable spot
        otherwise, if the cell is empty or out of bounds
            return False, to indicate no valid capture was found
    
    for each of the 8 possible directions
        call helper with this direction and the current position

"""


def reversi(board, color, x, y):

    if not board:
        return

    oppositeColor = "W" if color == "B" else "B"
    emptyVal = "*"
    
    n = len(board)
    m = len(board[0])

    # Process in eight directions
    # combination([-1,0,1], 2)
    # directions.remove((0,0))

    directions = [
        (-1, -1), (0, -1), (+1, -1),
        (-1,  0),          (+1,  0),
        (-1, +1), (0, +1), (+1, +1),
    ]

    def checkBound(ix, iy) -> bool:
        return not (ix < 0 or ix >= n or iy < 0 or iy >= m)

    # See if a direction should be flipped
    def find(ix, iy, xd, xy, toFlip):

        oob = not checkBound(ix, iy)

        if oob:
            return

        val = board[ix][iy]

        # if coordinate value is OOB or empty, end
        if val == emptyVal:
            return

        # if coordinate value is opposite, continue
        if val == oppositeColor:
            toFlip.append((ix, iy))
            find(ix + xd, iy + yd, xd, xy, toFlip)
        else:
            # if coordinate value is color, flip toFlip
            for flipCoordinate in toFlip:
                fx, fy = flipCoordinate
                board[fx][fy] = color

    if not checkBound(x, y):
        return

    for direction in directions:
        xd, yd = direction

        find(x + xd, y + yd, xd, yd, [])
    
    return board

