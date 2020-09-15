from typing import List

class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:

        stack = []

        while pushed:

            # take an element from pushed
            stack.append(pushed.pop(0))

            # if top element of stack matches fron element of popped, pop both
            while stack and popped and popped[0] == stack[-1]:
                popped.pop(0)
                stack.pop()

        return not pushed and not popped
        

if __name__ == "__main__":
    s = Solution()
    input =([1,2,3,4,5], [4,5,3,2,1])
    print(s.validateStackSequences(input[0],input[1])) # True

    input =([1,0,2], [2,1,0])
    print(s.validateStackSequences(input[0],input[1])) # True