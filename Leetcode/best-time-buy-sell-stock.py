from typing import List

class Solution:

    def maxProfit(self, prices: List[int]) -> int:

        buyAt, sellAt, nextBuyAt = 0, 0, 0

        def profit(buyAt: int, sellAt:int) -> int:
            if buyAt >= sellAt: return 0
            return prices[sellAt] - prices[buyAt]
        
        for idx, price in enumerate(prices):
            if profit(nextBuyAt, idx) > profit(buyAt, sellAt):
                buyAt = nextBuyAt
                sellAt = idx
            if price < prices[buyAt]:
                nextBuyAt = idx
            
        return profit(buyAt, sellAt)

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) # 5
    print(s.maxProfit([7,6,4,3,1])) # 0
