# Write any import statements here

def getSum(A: int, B: int, C: int) -> int:
  res = A + B + C
  return res

def getWrongAnswers(N: int, C: str) -> str:

  res = ""

  for i in range(N):

    if i >= len(C):
      break

    # Get ith char in C
    c = C[i]

    # Append opposite char to res
    if c == 'A':
      res = res + 'B'
    else:
      res = res + 'A'
    
  return res

from typing import List
# Write any import statements here

def getHitProbability(R: int, C: int, G: List[List[int]]) -> float:

  total = R * C
  ships = 0

  for list in G:
    ships = ships + list.count(1)
  
  probability = ships / total

  # Write your code here
  return probability

def printString(string):
  print('[\"', string, '\"]', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printString(expected)
    print(' Your output: ', end='')
    printString(output)
    print()
  test_case_number += 1

# if __name__ == "__main__":
#   input_1 = "AAAAAA"
#   n_1 = 4
#   expected_1 = "BBBB"
#   output_1 = getWrongAnswers(n_1, input_1)
#   check(expected_1, output_1)

# if __name__ == "__main__":
#   input_1 = (2, 3, [[0, 0, 1], [1, 0, 1]])
#   expected_1 = 0.5
#   output_1 = getHitProbability(input_1[0], input_1[1], input_1[2],)
#   check(expected_1, output_1)