# You are playing the Bulls and Cows game with your friend.

# You write down a secret number and ask your friend to guess what the number is. When your friend makes a guess, you provide a hint with the following info:

# The number of "bulls", which are digits in the guess that are in the correct position.
# The number of "cows", which are digits in the guess that are in your secret number but are located in the wrong position. Specifically, the non-bull digits in the guess that could be rearranged such that they become bulls.
# Given the secret number secret and your friend's guess guess, return the hint for your friend's guess.

# The hint should be formatted as "xAyB", where x is the number of bulls and y is the number of cows. Note that both secret and guess may contain duplicate digits.

# Iterate through secret

# Is bull:
#     count
# If not bull,
#     Collect/count digit in secret
#     Collect/count digit in guess

# Go through every digit in guess and see if there was a corresponding unmatched digit seen in secret

from collections import defaultdict

class Solution:
    def getHint(self, secret: str, guess: str) -> str:

        sCounts = defaultdict(int)
        gCounts = defaultdict(int)

        bulls = 0
        cows = 0

        # O(N) time O(N) space
        for idx, s in enumerate(secret):

            g = guess[idx]

            if s == g:
                bulls += 1
            else:
                sCounts[s] += 1
                gCounts[g] += 1
        
        for key in gCounts.keys():

            g = gCounts[key]
            s = sCounts[key]

            cows += min(g, s)
        
        ans = str(bulls) + "A" + str(cows) + "B"
        print(ans)
        return ans



assert Solution().getHint(secret = "1807", guess = "7810") == "1A3B"
assert Solution().getHint(secret = "1123", guess = "0111") == "1A1B"
assert Solution().getHint(secret = "112222", guess = "100111") == "1A1B"


# Example 1:

# Input: secret = "1807", guess = "7810"
# Output: "1A3B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1807"
#   |
# "7810"
# Example 2:

# bulls: same value same position
# cows: same value diff position

# Input: secret = "1123", guess = "0111"
# Output: "1A1B"
# Explanation: Bulls are connected with a '|' and cows are underlined:
# "1123"        "1123"
#   |      or     |
# "0111"        "0111"
# Note that only one of the two unmatched 1s is counted as a cow since the non-bull digits can only be rearranged to allow one 1 to be a bull.
 

# Constraints:

# 1 <= secret.length, guess.length <= 1000
# secret.length == guess.length
# secret and guess consist of digits only.
