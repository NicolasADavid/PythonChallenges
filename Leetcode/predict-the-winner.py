from typing import List
from collections import defaultdict
class Solution:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        
        def maxDiff(left, right):
            if left == right:
                return nums[left]
            score_by_left = nums[left] - maxDiff(left + 1, right)
            score_by_right = nums[right] - maxDiff(left, right - 1)
            return max(score_by_left, score_by_right)
        
        return maxDiff(0, n - 1) >= 0
    
class Solution2:
    def predictTheWinner(self, nums: List[int]) -> bool:
        n = len(nums)
        memo = defaultdict(int)
        
        def maxDiff(left, right):
            if (left, right) in memo:
                return memo[(left, right)]
            if left == right:
                return nums[left]
            score_by_left = nums[left] - maxDiff(left + 1, right)
            score_by_right = nums[right] - maxDiff(left, right - 1)
            
            memo[(left, right)] = max(score_by_left, score_by_right)
            return memo[(left, right)]
        
        return maxDiff(0, n - 1) >= 0
print(Solution2().predictTheWinner([10,24,5,9]))


# DP Solution
def max_profit(coins):
    n = len(coins)
    profit = [[0 for _ in range(n)] for _ in range(n)]

    for i in range(n):
        profit[i][i] = coins[i]

    for i in range(n - 1):
        profit[i][i + 1] = max(profit[i][i], profit[i + 1][i + 1])

    for gap in range(2, n):
        for i in range(n - gap):
            j = i + gap
            left = profit[i][j - 2]
            diagonal = profit[i + 1][j - 1]
            bottom = profit[i + 2][j]
            profit[i][i + gap] = max(
                coins[i] + min(diagonal, bottom),
                coins[j] + min(left, diagonal)
            )

    return profit[0][-1]
# print(max_profit([10,24,5,9]))