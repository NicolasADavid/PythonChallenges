import math
# Add any extra import statements you may need here

# Add any helper functions you may need here

#LR [0, 0, 2, 0, 4]
#RL [1, 0, 1, 0, 0]

#S  [(3, 0)]
#S  [(3, 0), (1, 0)]
#S  [(7, 2), (2, 0)]
#S  [(9, 4)]

#O  [2, 1, 4, 1, 5]
#I  [3, 1, 7, 2, 9]

def count_subarrays(arr):

    # l = len(arr)
    # Write your code here

    # Go from left to right, then right to left
    # Build auxilliary array, which is how many numbers to the right or left of arr[i] are less than arr[i]
    # Use stack to track numbers and how many numbers before are less than the number, folding in when larger numbers are encountered
    # At each position, save how many to the right or left are less than num at position. This is lessThan in (number, lessThan), which is the tuple
    # pushed into the stack

    # Each position's output is 1 + leftToRight + rightToLeft

    leftToRight = []
    stack = []
    for i in range(len(arr)):

        n = arr[i]

        sum = 0

        while stack and stack[-1][0] < n:
            popped = stack.pop()
            sum += 1 + popped[1]

        stack.append((n, sum))
        leftToRight.append(sum)

    rightToLeft = []
    stack = []
    for i in reversed(range(len(arr))):

        n = arr[i]

        sum = 0

        while stack and stack[-1][0] < n:
            popped = stack.pop()
            sum += 1 + popped[1]

        stack.append((n, sum))
        rightToLeft.append(sum)

    rightToLeft = list(reversed(rightToLeft))

    output = []
    for i in range(len(arr)):
        output.append(1 + leftToRight[i] + rightToLeft[i])
    
    return output

# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

def printIntegerList(array):
  size = len(array)
  print('[', end='')
  for i in range(size):
    if i != 0:
      print(', ', end='')
    print(array[i], end='')
  print(']', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  expected_size = len(expected)
  output_size = len(output)
  result = True
  if expected_size != output_size:
    result = False
  for i in range(min(expected_size, output_size)):
    result &= (output[i] == expected[i])
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printIntegerList(expected)
    print(' Your output: ', end='')
    printIntegerList(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
  test_1 = [3, 4, 1, 6, 2]
  expected_1 = [1, 3, 1, 5, 1]
  output_1 = count_subarrays(test_1)
  check(expected_1, output_1)
  
  test_2 = [2, 4, 7, 1, 5, 3]
  expected_2 = [1, 2, 6, 1, 3, 1]
  output_2 = count_subarrays(test_2)
  check(expected_2, output_2)

  # Add your own test cases here
  