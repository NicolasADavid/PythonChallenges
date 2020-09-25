from typing import List

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buyAt = 0
        sellAt = 0
        nextBuyAt = 0
        nextSellAt = 0

        def profit(buy, sell) -> int:

            if buy >= sell: return 0

            return prices[sell] - prices[buy]

        for i, price in enumerate(prices):
            if price < prices[nextBuyAt]:
                nextBuyAt = nextSellAt = i
            if price > prices[nextSellAt]:
                nextSellAt = i

            if profit(nextBuyAt, nextSellAt) > profit(buyAt, sellAt):
                buyAt = nextBuyAt
                sellAt = nextSellAt

        return profit(buyAt, sellAt)

if __name__ == "__main__":
    s = Solution()
    print(s.maxProfit([7,1,5,3,6,4])) # 5
    print(s.maxProfit([7,6,4,3,1])) # 0
