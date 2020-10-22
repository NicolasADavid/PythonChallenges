import math
# Add any extra import statements you may need here

from collections import defaultdict
from collections import Counter

# Add any helper functions you may need here

# Start left and right at 0
# Create counter of chars in t
# Create counter for chars in s
# Add char at s[0] to counter
# Check if sum(c = countT - countS) == 0
# If solves, track best
# Best is solution with min(right - left)
# If solves, decr s[left] from countS and incr left
# If does not solve, incr right
# Continue until right reaches end
# Sliding Window

def min_length_substring(s, t):

    if not t:
        return 0

    ct = dict(Counter(t))
    cs = defaultdict(int)

    left = right = 0

    new = s[left]
    cs[new] = cs[new] + 1

    best = None

    while right < len(s):
        c = Counter(ct) - Counter(cs)
        if sum(c.values()) == 0:
            ansLen = right-left+1
            best = min(best, ansLen) if best else ansLen
            removed = s[left]
            cs[removed] = cs[removed] - 1
            left += 1
            continue

        right += 1
        if right < len(s):
            new = s[right]
            cs[new] = cs[new] +1
    
    return best if best else -1

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

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
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  s1 = "dcbefebce"
  t1 = "fd"
  expected_1 = 5
  output_1 = min_length_substring(s1, t1)
  check(expected_1, output_1)

  s2 = "bfbeadbcbcbfeaaeefcddcccbbbfaaafdbebedddf"
  t2 = "cbccfafebccdccebdd"
  expected_2 = -1
  output_2 = min_length_substring(s2, t2)
  check(expected_2, output_2)

	# Add your own test cases here
  