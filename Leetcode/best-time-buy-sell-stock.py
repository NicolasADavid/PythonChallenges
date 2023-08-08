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
            if price < prices[nextBuyAt]:
                nextBuyAt = idx
            
        return profit(buyAt, sellAt)

class Solution2:
    def maxProfit(self, prices: List[int]) -> int:
        min_price = float('inf')
        max_profit = 0
        for i in range(len(prices)):
            if prices[i] < min_price:
                min_price = prices[i]
            elif prices[i] - min_price > max_profit:
                max_profit = prices[i] - min_price
                
        return max_profit

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) # 5
    print(s.maxProfit([7,6,4,3,1])) # 0
    print(s.maxProfit([4,7,1,2,11])) # 10
