"""
Coin Change Number of Ways

You are given coins of different denominations and a total amount of money. Write a function to compute the "number of combinations" that make up that amount.
 

EXAMPLE(S)
Input: amount = 5, coins = [1, 2, 5]
Output: 4
Explanation: there are four ways to make up the amount:
5=5
5=2+2+1
5=2+1+1+1
5=1+1+1+1+1

Input: amount = 3, coins = [2]
Output: 0
Explanation: the amount of 3 cannot be made up just with coins of 2.

Input: amount = 10, coins = [10] 
Output: 1
 

FUNCTION SIGNATURE
func coinChangeCombinations(coins: [Int], amount: Int) -> 



Recursive (Top-down)

Given a target price
Base case: negative (0) or 0 (1)
Answer is how many ways (price - C1) + (price - C2) + ... (price - CN)
Summing:
    For every coin, subtract coin value from price, sum function(new price)
return sum

-X: 0
0: 1
1: R(..)

Dynamic (Botton-up)




"""
from typing import List

x = 0

def coin_change_combos(coins: list[int], amount: int, start = 0) -> int:

    global x
    x += 1

    # print("Make change for amount:", amount, "with coins:", coins[start:])

    if amount < 0:
        return 0

    if amount == 0:
        return 1

    result = 0
    for i in range(start, len(coins)):
        # print( "subtract: " , coins[i], " from: ", amount)

        result += coin_change_combos(coins, amount - coins[i], i)

    # print("Returning result:", result, "for amount:", amount, "with coins:", coins[start:])

    return result

# assert coin_change_combos([5], 5) == 1
# assert coin_change_combos([1, 5], 5) == 2
# assert coin_change_combos([1, 2, 5], 5) == 4
# assert coin_change_combos([1, 2, 5], 0) == 1
# assert coin_change_combos([], 5) == 0
# assert coin_change_combos([5, 10], 3) == 0
# assert coin_change_combos([1, 2, 5], 10) == 10
# assert coin_change_combos([1, 5, 10, 25, 50], 100) > 0
# assert coin_change_combos([2, 3, 5], 7) == 2

print("Total recursive calls:", x)

from functools import lru_cache
from typing import Tuple

y = 0

@lru_cache(maxsize=None)
def coin_change_combos_lru(coins: Tuple[int], amount: int, start = 0) -> int:

    global y
    y += 1

    # print("Make change for amount:", amount, "with coins:", coins[start:])

    if amount < 0:
        return 0

    if amount == 0:
        return 1

    result = 0
    for i in range(start, len(coins)):
        # print( "subtract: " , coins[i], " from: ", amount)

        result += coin_change_combos_lru(coins, amount - coins[i], i)

    # print("Returning result:", result, "for amount:", amount, "with coins:", coins[start:])

    return result

# assert coin_change_combos_lru((5,), 5) == 1
# assert coin_change_combos_lru((1, 5), 5) == 2
# assert coin_change_combos_lru((1, 2, 5), 5) == 4
# assert coin_change_combos_lru((1, 2, 5), 0) == 1
# assert coin_change_combos_lru((), 5) == 0
# assert coin_change_combos_lru((5, 10), 3) == 0
# assert coin_change_combos_lru((1, 2, 5), 10) == 10
# assert coin_change_combos_lru((1, 5, 10, 25, 50), 100) > 0
# assert coin_change_combos_lru((2, 3, 5), 7) == 2

print("Total recursive calls w/ LRU:", y)

def coin_change_combos_dp(coins: List[int], amount: int) -> int:

    dp = [0 for _ in range(amount + 1)]
    # There's only one way to reach an amount of 0 - no coins
    dp[0] = 1

    for coin in coins:
        for i in range(1, amount + 1):
            if i - coin >= 0:
                dp[i] += dp[i-coin]

    return dp[amount]

assert coin_change_combos_dp([5], 5) == 1
assert coin_change_combos_dp([1, 5], 5) == 2
assert coin_change_combos_dp([1, 2, 5], 5) == 4
assert coin_change_combos_dp([1, 2, 5], 0) == 1
assert coin_change_combos_dp([], 5) == 0
assert coin_change_combos_dp([5, 10], 3) == 0
assert coin_change_combos_dp([1, 2, 5], 10) == 10
assert coin_change_combos_dp([1, 5, 10, 25, 50], 100) > 0
assert coin_change_combos_dp([2, 3, 5], 7) == 2