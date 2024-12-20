# Dynamic Programming

# Dynamic programming is technique or genre of solution — it's not right to call it an algorithm — that appleis when your problem meets two conditions:
# 1. Optimal Substructure
# 2. Overlapping Subpriblems

# Dynamic Programming Practice

def fib_bottom_up(n):
    if n < 2:
        return n

    memo = [0,1]

    for i in range(2, n+1):
        tmp = memo[1]
        memo[1] = memo[0] + memo[1]
        memo[0] = tmp
        continue
    
    return memo[1]


from functools import lru_cache

# @lru_cache()
def fib(n):
    if n < 2:
        return n
    
    return fib(n - 1) + fib(n - 2)

# print(fib_bottom_up(10))
print(fib(10))

# ### Counting Stairs

# Imagine a staircase with N stairs. If it's easier, imagine a specific number like N=100 or N=10.

# Your legs are long enough that you can climb the stairs by going up one step or by skipping a step and going up two steps.

# How many ways are there to get to the top of the stairs?


def stairs(n, memo = None):
    if memo is None:
        memo = {}

    if n in memo:
        return memo[n]

    if n == 0:
        return 0
    if n == 1:
        return 1
    
    # if n === 3:
    #     return 4

    memo[n] = stairs(n-1, memo) + stairs(n-2, memo)
    return memo[n]

import pickle

_cache = dict()
def memoize(f):
    """Memoize any function."""

    def decorated(*args):
        key = (f, pickle.dumps(args))
        if key in _cache:
            return _cache[key]

        _cache[key] = f(*args)
        return _cache[key]

    return decorated


# There are 42 ways to go up 98 steps
# There are 54 ways to go up 99 steps

fib = memoize(fib)
print(fib(100))