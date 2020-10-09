from collections import defaultdict
from collections import Counter

# Start left and right at 0
# Create counter of chars in t
# Create counter for chars in s
# Add char at s[0] to counter
# Check if sum(c = countT - countS) == 0
# If solves, track best
# Best is solution with min(right - left)
# If solves, decr s[left] from countS and incr left
# If does not solve, incr right
# Continue until right reaches end

class Solution:

    def minWindow(self, s: str, t: str) -> str:

        if not t:
            return 0

        ct = dict(Counter(t))
        cs = defaultdict(int)

        left = right = 0

        new = s[left]
        cs[new] = cs[new] + 1

        best = None
        idxs = (0, 0)

        while right < len(s):
            c = Counter(ct) - Counter(cs)
            if sum(c.values()) == 0:
                l = right - left + 1

                if not best or best > l:
                    best = l
                    idxs = (left, right)

                removed = s[left]
                cs[removed] = cs[removed] - 1
                left += 1
                continue

            right += 1
            if right < len(s):
                new = s[right]
                cs[new] = cs[new] +1
        
        return s[idxs[0]:idxs[1]+1] if best else ""