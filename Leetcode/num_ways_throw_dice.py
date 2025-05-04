'''
You given a total number of dice, the number of faces on each dice and a total, write a function that determines the total number of ways to throw the dice to get the target sum.

If the number of faces on a dice is X, then numbers on each face will be 1, 2, ..., X. So a dice with 5 faces will have numbers 1, 2, 3, 4 and 5.
 

EXAMPLE(S)
n = 1, faces = 6, total = 3 returns 1 (must throw face 3)
n = 3, faces = 6, total = 7 returns 15

Spoiler examples (reveals expected questions)
n = 2, faces = 5, total = 8 returns  3 (4, 4 or 3, 5 or 5, 3)
 
backtracking: O(f^n)

[1,0,0,0,0,0]
[1,1,0,0,0,0]

  0 1 2 3 4 5 6 7 8
0  0 0 0 0 0 0 0 0
1  1 1 1 1 1 1 0 0
2 0 1 


FUNCTION SIGNATURE
def number_ways(n, faces, total) 
'''
'''
NUM(n, f, t)

NUM(n, f, t | t < 0) = 0
NUM(n, f, t | f > t and n == 1) = 1
NUM(n, f, t | t > n*f) = 0
NUM(0, f, t | t > 0) = 0
NUM(0, f, 0) = 1


NUM(n, f, t | t < n) = 0
NUM(n, f, t | n > 1) =  NUM(n-1, f, t-1) + NUM(n-1,f,t-2) + ... + NUM(n-1, f, t-f)

cache[n][t]
cache[n%2][t]
'''

# from functools import cache
# @cache

c = {} # (n, f, t) -> value ?
# c[(n,t)]

def numWays_uncached(n,f,t):
  if t < 0:
    return 0

  if n == 0 and t > 0:
    return 0

  if n == 0 and t == 0:
    return 1
    
  count = 0
  for val in range(1, f+1):
    count += numWays(n-1,f,t-val)

  return count

def numWays(n,f,t):
  if (n,f,t) in c:
    return c[(n,f,t)]
  c[(n,f,t)] = numWays_uncached(n,f,t)
  return c[(n,f,t)]
  
  


# Recursive
def number_ways_recursive(n, faces, target):
    if target < 1:
        return 0

    if n == 1:
        return 1 if target <= faces else 0

    total = 0
    for f in range(1, faces + 1):
        total += number_ways_recursive(n - 1, faces, target - f)

    return total


# Dynamic
def number_ways_dp(n, faces, target):
    dp = [[0] * (target + 1) for _ in range(n + 1)]
    dp[0][0] = 1

    # for i in range(1, n + 1):
    #     for j in range(1, target + 1):
    #         for f in range(1, min(faces, j) + 1):
    #             dp[i][j] += dp[i - 1][j - f]

    for dice_num in range(1, n + 1):
        for target_sum in range(1, target + 1):
            for dice_value in range(1, min(faces, target_sum) + 1):
                print(f"Dice_num: {dice_num}\t target_sum: {target_sum}\t dice_value: {dice_value}")
                dp[dice_num][target_sum] += dp[dice_num - 1][target_sum - dice_value]

    r =  dp[n][target]
    return r

# print(c)
# print(numWays(1,6,3))
# print(number_ways_dp(1,6,3))
# print(numWays(2,5,8))
# print(number_ways_dp(2,5,8))
# print(numWays(3,6,7))
# print(number_ways_dp(3,6,7))
# print(number_ways_dp(5,6,7))
# print(number_ways_dp(5,6,20))
# print(number_ways_dp(10,6,20))
# print(number_ways_dp(10,45,200))

val = number_ways_dp(10,50,200)

places = len(str(val))

if places > 0 and places < 4:
   print("thousand")
elif places > 3 and places < 7:
   print("million")
elif places > 6 and places < 10:
    print("billion")
elif places > 9 and places < 13:
   print("trillion")
elif places > 12 and places < 16:
    print("quadrillion")
elif places > 15 and places < 19:
    print("quintillion")
elif places > 18 and places < 22:
    print("sextillion")
elif places > 21 and places < 25:
    print("septillion") 
elif places > 24 and places < 28:
    print("octillion")
elif places > 27 and places < 31:
    print("nonillion")
elif places > 30 and places < 34:
    print("decillion")
elif places > 33 and places < 37:
    print("undecillion")
elif places > 36 and places < 40:
   print("duodecillion")