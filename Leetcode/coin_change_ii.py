class Solution(object):
    def change(self, amount, coins):
        """
        :type amount: int
        :type coins: List[int]
        :rtype: int
        """
        
        dp = [0] * (amount + 1)
        dp[0] = 1

        for coin in coins:
            for i in range(coin, amount + 1):
                dp[i] += dp[i - coin]

        return dp[amount]
    
if __name__ == "__main__":
    amount = 5
    coins = [1,2,5]
    assert Solution().change(amount, coins) == 4

    amount = 3
    coins = [2]
    assert Solution().change(amount, coins) == 0

    amount = 10
    coins = [10]
    assert Solution().change(amount, coins) == 1
    amount = 0
    coins = [1]
    assert Solution().change(amount, coins) == 1
    amount = 1
    coins = [1]
    assert Solution().change(amount, coins) == 1
    amount = 2
    coins = [1]
    assert Solution().change(amount, coins) == 1