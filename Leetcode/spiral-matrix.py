from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
      if not matrix:
        return []
      
      h = len(matrix)
      w = len(matrix[0])
      n = h * w
      ans = []

      fromtop = 0
      fromright = 0
      frombottom = 0
      fromleft = 0
      
      while n > 0:
        #left to right
        for i in range(fromleft, w - fromright):
          ans.append(matrix[fromtop][i])
          n = n-1
          if n == 0: return ans
        fromtop = fromtop + 1
          
        #top to bottom
        for i in range(fromtop, h - frombottom):
           ans.append(matrix[i][w - 1 - fromright])
           n = n-1
           if n == 0: return ans
        fromright = fromright + 1

        #right to left
        for i in reversed(range(fromleft, w - fromright)):
           ans.append(matrix[h - 1 - frombottom][i])
           n = n-1
           if n == 0: return ans
        frombottom = frombottom + 1

        #bottom to top
        for i in reversed(range(fromtop, h - frombottom)):
           ans.append(matrix[i][fromleft])
           n = n-1
           if n == 0: return ans
        fromleft = fromleft + 1

      return ans
       

    def spiralOrder1(self, matrix: List[List[int]]) -> List[int]:

        if not matrix: return []
    
        skipUp = 0
        skipDown = 0
        skipLeft = 0
        skipRight = 0

        h = len(matrix)
        w = len(matrix[0])

        n = h * w
        ops = 0
        res = []

        while ops < n:
            # ltr
            for i in range(0 + skipLeft, w - skipRight):
                res.append(matrix[skipUp][i])
                ops += 1
                if ops == n: return res
            skipUp += 1

            # ttb
            for i in range(0 + skipUp, h - skipDown):
                res.append(matrix[i][w - 1 - skipRight])
                ops += 1
                if ops == n: return res
            skipRight += 1

            # rtl
            for i in reversed(range(0 + skipLeft, w - skipRight)):
                res.append(matrix[h - 1 - skipDown][i])
                ops += 1
                if ops == n: return res
            skipDown += 1

            # btt
            for i in reversed(range(0 + skipUp, h - skipDown)):
                res.append(matrix[i][skipLeft])
                ops += 1
                if ops == n: return res
            skipLeft += 1

        return res


# if __name__ == "__main__":
#     s = Solution()
#     r = s.spiralOrder(matrix = [[1,2,3],[4,5,6],[7,8,9]])
#     print(r)

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

if __name__ == "__main__":

    s = Solution()

    input_1 = [[1,2,3],[4,5,6],[7,8,9]]
    expected_1 = [1,2,3,6,9,8,7,4,5]
    output_1 = s.spiralOrder(input_1)
    check(expected_1, output_1)

    input_2 = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
    expected_2 = [1,2,3,4,8,12,11,10,9,5,6,7]
    output_2 = s.spiralOrder(input_2)
    check(expected_2, output_2)
  