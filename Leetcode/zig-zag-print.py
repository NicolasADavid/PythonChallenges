'''
Given a string an a positive number of rows, consider this method of formatting the string across the prescribed number of rows. If the original string is FORMATION and we want 3 rows, then the first three characters are down the first column as so:

F
O
R

The next character, M, diagonals up so then is next to the O. The A then continues up and to the right on the first row before proceeding down with the column:

F   A
O M T
R   I

The final two letters continue the pattern:

F   A   N
O M T O
R   I

Now, if we read these letters in the normal fashion (left to right, top down), we get FANOMTORI.

With 4 rows, we'd get:

F     I
O   T O
R A   N
M

And then read in normal fashion we'd get FIOTORANM.

Write a function that computes this reordering.
 

EXAMPLE(S)
toZigzag("FORMATION", 3) -> FANOMTORI
toZigzag("FORMATION", 4) -> FIOTORANM
 

FUNCTION SIGNATURE
function toZigzag(s, numRows)
def to_zigzag(s, num_rows):



Create a stack for each desired column

Outer loop continue for each char
    while loop for going down
    while loop for going up

return Concat(row1 + row2 + row3)




'''

def to_zigzag(s, num_rows):

    if num_rows == 1:
        return s

    rows = [[] for _ in range(num_rows)]

    idx = 0 # rowIdx
    charIdx = 0

    while charIdx < len(s):

        # going down
        while idx != num_rows and charIdx<len(s):
            rows[idx].append(s[charIdx])
            charIdx += 1
            idx += 1

        idx -= 2

        # going up
        while idx != -1 and charIdx<len(s):
            rows[idx].append(s[charIdx])
            charIdx += 1
            idx -= 1
        
        idx += 2

    ans = []

    for row in rows:
        for char in row:
            ans.append(char)

    return "".join(ans)

'''
assert to_zigzag("FORMATION", 4) == "FIOTORANM"

 F 0
 O 1
 R 2
 M 3
 A 4
 T 5
 I 6
 O 7
 N 8

06 -> 6
157 -> 4, 2
248 -> 2, 4
3 -> ??

F     I
O   T O
R A   N
M
'''

def to_zigzag(s, num_rows):
  if num_rows == 1: return s
  chars = []
  repeat_size = num_rows * 2 - 2
  num_chars = len(s)

  for r in range(num_rows):
    for i in range(r, num_chars, repeat_size):
      chars.append(s[i])
      if r > 0 and r < num_rows - 1 and i + repeat_size - 2*r < num_chars:
        chars.append(s[i + repeat_size - 2*r])
  return "".join(chars)


assert to_zigzag("FORMATION", 3) == "FANOMTORI"
assert to_zigzag("FORMATION", 4) == "FIOTORANM"


# test 1 rows (1 char)
assert to_zigzag("F", 1) == "F"
# test 1 rows (2 char)
# test 1 rows (10 char)

# test 2 rows (1 char)
assert to_zigzag("F", 2) == "F"

# test 2 rows (2 char)
# test 2 rows (10 char)
assert to_zigzag("FORMATION", 2) == "FRAINOMTO"


# test 4 rows (1 char)
# test 4 rows (2 char)
# test 4 rows (10 char)


def convert(self, s: str, numRows: int) -> str:
    if(numRows == 1):
        return s
    if(s != None and numRows > 1):
        out = ''
        substringlen = numRows + numRows - 2
        for x in range(numRows):
            index = x
            numtoincrement = (numRows - x) + ((numRows - x) - 2)
            high = substringlen - 1
            count = 1
            while (index < len(s)):
                if(count <= 2):
                    out = '%s%s' % (out, s[index])
                    if(numtoincrement>0):
                        newindex = index + numtoincrement
                    else:
                        newindex = -1
                    if(newindex > high or newindex == -1):
                        index = x + high + 1
                        high = high + substringlen
                        count = 1
                    else:
                        index = newindex
                        count = count + 1
                else:
                    index = x + high + 1
                    high = high + substringlen
                    count = 1
        return out
    else:
        return None



