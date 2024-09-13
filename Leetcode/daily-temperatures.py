from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        n = len(temperatures)
        out = [0] * n
        stack = []


        for i, temp in enumerate(temperatures):

            while stack and temp > temperatures[stack[-1]]:

                # How many days later to encounter a higher temperature
                out[stack[-1]] = i - stack[-1]

                stack.pop()

            stack.append(i)

        return out


print(Solution().dailyTemperatures([73,74,75,71,69,72,76,73]))