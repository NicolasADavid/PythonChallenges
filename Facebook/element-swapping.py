# Element Swapping
# Given a sequence of n integers arr, determine the lexicographically smallest sequence which may be obtained from it after performing at most k element swaps, each involving a pair of consecutive elements in the sequence.
# Note: A list x is lexicographically smaller than a different equal-length list y if and only if, for the earliest index at which the two lists differ, x's element at that index is smaller than y's element at that index.
# Signature
# int[] findMinArray(int[] arr, int k)
# Input
# n is in the range [1, 1000].
# Each element of arr is in the range [1, 1,000,000].
# k is in the range [1, 1000].
# Output
# Return an array of n integers output, the lexicographically smallest sequence achievable after at most k swaps.
# Example 1
# n = 3
# k = 2
# arr = [5, 3, 1]
# output = [1, 5, 3]
# We can swap the 2nd and 3rd elements, followed by the 1st and 2nd elements, to end up with the sequence [1, 5, 3]. This is the lexicographically smallest sequence achievable after at most 2 swaps.
# Example 2
# n = 5
# k = 3
# arr = [8, 9, 11, 2, 1]
# output = [2, 8, 9, 11, 1]
# We can swap [11, 2], followed by [9, 2], then [8, 2].

import math

def findMinArray(arr, k):
  left = 0
  
  minIdx = left
  
  while k > 0 and left < len(arr):
  
    for i in range(left, min(left + k + 1, len(arr))):
      # find minimum element within k steps from left pointer

      # Found an element smaller than element at minIdx
      if arr[i] < arr[minIdx]:
        minIdx = i
  
    # move min element up. Min can move 0 steps.
    moves = minIdx - left
    
    # How to move an element up correctly?
    # Bubble forward element at minIdx
    for i in range(moves):
      moveFrom = minIdx - 1
      moveBack = arr[moveFrom]
      
      arr[moveFrom] = arr[minIdx]
      arr[minIdx] = moveBack
      minIdx -= 1
    
    # Decrement k by moves used
    # Increment left
    k -= moves
    left += 1
    minIdx = left

  return arr

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
  n_1 = 3
  arr_1 = [5, 3, 1]
  k_1 = 2 
  expected_1 = [1, 5, 3]
  output_1 = findMinArray(arr_1,k_1)
  check(expected_1, output_1)

  n_2 = 5
  arr_2 = [8, 9, 11, 2, 1]
  k_2 = 3
  expected_2 = [2, 8, 9, 11, 1]
  output_2 = findMinArray(arr_2,k_2)
  check(expected_2, output_2)
    
  n_3 = 5
  arr_3 = [5,4,3,2,1]
  k_3 = 10
  expected_3 = [1,2,3,4,5]
  output_3 = findMinArray(arr_3,k_3)
  check(expected_3, output_3)
    
  n_4 = 5
  arr_4 = [5,4,3,2,1]
  k_4 = 11
  expected_4 = [1,2,3,4,5]
  output_4 = findMinArray(arr_4,k_4)
  check(expected_4, output_4)
    
  n_5 = 5
  arr_5 = [1,1,1,1,1]
  k_5 = 11
  expected_5 = [1,1,1,1,1]
  output_5 = findMinArray(arr_5,k_5)
  check(expected_5, output_5)
    
  n_6 = 1
  arr_6 = [1]
  k_6 = 100
  expected_6 = [1]
  output_6 = findMinArray(arr_6,k_6)
  check(expected_6, output_6)
    
  n_7 = 5
  arr_7 = [1,2,1,2,1]
  k_7 = 3
  expected_7 = [1,1,1,2,2]
  output_7 = findMinArray(arr_7,k_7)
  check(expected_7, output_7)
    
  n_8 = 5
  arr_8 = [1,2,1,2,1]
  k_8 = 2
  expected_8 = [1,1,2,1,2]
  output_8 = findMinArray(arr_8,k_8)
  check(expected_8, output_8)

  # Add your own test cases here
  