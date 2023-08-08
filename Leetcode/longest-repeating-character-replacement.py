from collections import defaultdict
class Solution:
    def characterReplacement(self, s: str, k: int) -> int:

        if not s:
            return 0

        l, r, best, subs = 0, 0, 0, 0
        letter = s[0]

        # track counts of letters seen
        counts = defaultdict(int)
        counts[letter] = 1


        while r < len(s):

            # check solution
            if subs <= k:
                best = max(best, r - l + 1)

                # expand
                r += 1

                # boundary
                if r == len(s):
                    break 

                addLetter = s[r]

                # add count for new letter
                counts[addLetter] = counts[addLetter] + 1

                # has best letter to use changed?
                if counts[letter] < counts[addLetter]:
                    letter = addLetter
                    subs = subs - counts[addLetter] + counts[letter]

                # track substitutions
                if s[r] != letter:
                    subs += 1
            else:

                # contract
                removeLetter = s[l]
                counts[removeLetter] = counts[removeLetter] - 1
                l += 1

                # determine next best letter to use
                letter = max(counts, key=counts.get)
                lettercount = counts[letter]

                sumOtherLetterCounts = sum(counts.values()) - lettercount
                subs = sumOtherLetterCounts

        return best

# print(Solution().characterReplacement(s = "ABAB", k = 2)) # 4
# print(Solution().characterReplacement(s = "AABABBA", k = 1)) # 4
# print(Solution().characterReplacement(s = "AABBBABBACCCCCCCS", k = 1)) # 4
print(Solution().characterReplacement(s = "ABBB", k = 1)) # 4