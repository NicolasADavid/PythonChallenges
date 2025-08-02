'''
Given an input N representing n number of stairs, compute the number of ways to reach the n'th stair if you can climb either 1 or 2 stairs at a time.
 

EXAMPLE(S)
Input: 1
Output: 1
Explanation: There is only one way to climb one stair: (1)

Input: 2
Output: 2
Explanation: There are 2 ways to climb 2 stairs: (1,1) and (2)

Input: 4
Output: 5
Explanation: Here are the ways to climb 4 stairs: (1,1,1,1), (1,1,2), (1,2,1), (2,2)
 

FUNCTION SIGNATURE
func numWaysToClimb(input: n) -> Int
'''

from typing import List

steps = [1, 2]

def num_ways_climb_stairs_r(n: int, steps: List[int]) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1
    
    total = 0

    for step in steps:
        if n - step >= 0:
            total += num_ways_climb_stairs_r(n - step, steps)
    
    return total

def num_ways_climb_stairs_dp(n: int, steps: List[int]) -> int:
    if n < 0:
        return 0
    if n == 0:
        return 1

    dp = [0] * (n + 1)
    dp[0] = 1

    for i in range(1, n + 1):
        for step in steps:
            if i - step >= 0:
                dp[i] += dp[i - step]

    return dp[n]



# assert num_ways_climb_stairs_r(1, steps) == 1
# assert num_ways_climb_stairs_dp(1, steps) == 1

assert num_ways_climb_stairs_r(2, steps) == 2
assert num_ways_climb_stairs_dp(2, steps) == 2

assert num_ways_climb_stairs_r(3, steps) == 3
assert num_ways_climb_stairs_dp(3, steps) == 3

assert num_ways_climb_stairs_r(4, steps) == 5
assert num_ways_climb_stairs_dp(4, steps) == 5

assert num_ways_climb_stairs_r(5, steps) == 8
assert num_ways_climb_stairs_dp(5, steps) == 8

assert num_ways_climb_stairs_r(20, steps) == 10946
assert num_ways_climb_stairs_dp(20, steps) == 10946


# numWaysToClimb(1) = 1
# numWaysToClimb(2) = 2
# numWaysToClimb(3) = 3
# numWaysToClimb(4) = 5
# numWaysToClimb(5) = 8
# numWaysToClimb(20) = 10946