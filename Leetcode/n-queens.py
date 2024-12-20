"""
function outer(outerArg1, outerArg2, ...) /* outerReturn */ {
  var results, innerVar1, innerVar2, ...;

  function isBad(solution) { ... }
  function isGood(solution) { ... }

  function inner(solution, innerArg1, innerArg2, ...) /* innerReturn */ {
    if (isBad(solution)) return;
    if (isGood(solution)) {
      results.push([...solution]);
      return;
    }

    for (let doMutate of ALL_CHANGE_FUNCS) {
      doMutate(solution); // modified currentSolution in place
      inner(solution);
      doMutate(solution, "undo"); // backtrack
    }
  }

  inner(emptySolution, innerArg1, ...)
  return result;
}
"""

[
    [".Q..","...Q","Q...","..Q."],
    ["..Q.","Q...","...Q",".Q.."]
    ]

from typing import List, Tuple

class Solution:

    def solveNQueens(self, n: int) -> List[Tuple[int, int]]:

        results = []

        def isBad(solution):
            if len(solution) <= 1: return False

            lqr, lqc = solution[-1]

            for (qr, qc) in solution[0:-1]:
                # O(q) two queens on same row
                # O(q) two queens on same column
                if lqr == qr or lqc == qc:
                    return True
            
                # O(q) two queens on same upward diagonal
                # O(q) two queens on same downward diagonal
                if abs(qr - lqr) == abs(qc - lqc):
                    return True
            
            return False

        def isGood(solution):
            return len(solution) == n

        def inner(solution):

            if isBad(solution):
                return
            
            if isGood(solution):
                results.append(list(solution))
                return

            for r in range(n):
                for c in range(n):
                    solution.append((r, c))
                    inner(solution)
                    solution.pop()


        inner([])

        def buildAnswerSet(solutions):

            answers = []

            for solution in solutions:

                answer = [["." for x in range(n)] for y in range(n)] 
                
                for r, c in solution:
                    answer[r][c] = "Q"

                def strJoinArr(arr):

                    # print("input: ", arr)

                    output = "".join(arr)

                    # print("output: ", output)

                    return output

                x = list(map(strJoinArr, answer))

                answers.append(x)

            return answers
                
        answers = buildAnswerSet(results)

        return answers


if __name__ == "__main__":
    # print(Solution().solveNQueens(1))
    print(Solution().solveNQueens(4))

"""

isBad:
    O(q) two queens on same row
    O(q) two queens on same column
    O(q) two queens on same upward diagonal
    O(q) two queens on same downward diagonal

isGood:
    do we have N queens on the board


_ _ 2 _ 
_ _ _ _ 
1 _ _ _ 
_ 3 _ _ 

1: 2,0
2: 0,2
3: 3,1

1 - 2 =>  2, -2 => 2, 2 => True
1 - 3 => -1,-1 => True

"""