'''
Today, you will be implementing git bisect.

Imagine a source control system that numbers each commits in sequential order. The first commit starts at 1. The next commit is at 2, and so on, until commit n.

At commit n, you've discovered that there's a bug in your program and you're trying to figure out which commit introduced the bug. You can assume that all commits after the first bad one are also bad.
 

EXAMPLE(S)
8 - bad
7 - bad
6 - bad
5 - good
4 - good
3 - good
2 - good
1 - good

For example, imagine that you have this situation, you would want to return 6, because it is the first bad commit.
 

FUNCTION SIGNATURE
function firstBadVersion(n)
def firstBadVersion(self, n: int) -> int:

The function takes the current commit number and returns the number of the first bad commit.



Current commit: most recent one. 
0 -> N (current) commits

Have a function available that tells us if a commit is good or not.
isBadVersion(int) -> bool
'''

def isBadVersion(n: int) -> bool:
    badVers = [x for x in range(6, 9)]

    return n in badVers


# 1   good
# 2   good
# 3   good
# 4   good
# 5   good <- 2nd step
# 6   good
# 7   good <- 3rd step
# 8   bad
# 9   bad
# 10  bad <- enter


# tgt = 6
# n = 8
def firstBadVersion(n: int) -> int:

    low = 1
    high = n

    ans = None

    def nextVersion() -> int:
        return low + ((high - low) // 2)

    def helper(version: int) -> None:

        nonlocal high
        nonlocal low
        nonlocal ans

        # version = 1: 8, 2: 4
        # high =    1: 8, 2: 8
        # low =     1: 0, 2: 0
    
        if isBadVersion(version):
            high = version
            # Is this the first bad version?
            # prev is None or is good
            if version == 1:
                ans = 1
            else:
                if not isBadVersion(version - 1):
                    ans = version
                else:
                # If bad version, look lower
                    helper(nextVersion())
        else:
        # If good version, look higher
            low = version
            helper(nextVersion())
    
    helper(n)

    return ans


print(firstBadVersion(8))


'''
Today, you will be implementing git bisect.

Imagine a source control system that numbers each commits in sequential order. The first commit starts at 1. The next commit is at 2, and so on, until commit n.

At commit n, you've discovered that there's a bug in your program and you're trying to figure out which commit introduced the bug. You can assume that all commits after the first bad one are also bad.
 

EXAMPLE(S)
8 - bad
7 - bad
6 - bad
5 - good
4 - good
3 - good
2 - good
1 - good

For example, imagine that you have this situation, you would want to return 6, because it is the first bad commit.
 

FUNCTION SIGNATURE
function firstBadVersion(n)
def firstBadVersion(self, n: int) -> int:

The function takes the current commit number and returns the number of the first bad commit.



Current commit: most recent one. 
0 -> N (current) commits

Have a function available that tells us if a commit is good or not.
isBadVersion(int) -> bool
'''

def firstBadVersion(n: int) -> bool:
    lo, hi = 1, n

    while lo < hi:
        mid = lo + ((hi-lo) // 2)
        # (hi + lo) // 2
        if isBadVersion(mid):
            hi = mid
        else:
            lo = mid + 1

    return lo

'''
8 - bad
7 - bad
6 - bad
5 - good
4 - good
3 - good
2 - good
1 - good

lo  hi  mid 
1   8   
1   8   4
5   8   6
5   6   5
6   6  

6
'''

'''
         
1 2 3 4 5 6 7 8 
         ^

'''

def lastGoodVersion(n: int) -> bool:
    lo, hi = 1, n

    while lo < hi:
        mid = (lo + hi + 1) // 2
        # (hi+lo) is an odd number, division: (1+4+1) // 2 == 3, pointer moves to the right, "ceiling" division
        # (hi+lo) is an even number, division: (1+3+1) // 2 == 2, same as (1+3) // 2, nothing changes
        if isBadVersion(mid):
            hi = mid - 1
        else:
            lo = mid

    return lo

'''
8 - bad
7 - bad
6 - bad
5 - good
4 - good
3 - good
2 - good
1 - good

lo  hi  mid 
1   8   
1   8   5
5   8   7
5   6   6
5   5  

5
'''
