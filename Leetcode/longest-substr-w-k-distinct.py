
from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        
        left = 0
        right = -1

        counts = defaultdict(int)
        distincts = 0
        best = 0
        
        while right < len(s):

            if distincts <= k:
                best = max(best, 1 + right - left)
            
            # Contract window
            if distincts > k:

                char = s[left]

                # Reduce count
                counts[char] = counts[char] - 1

                # If count went from 1 to 0, have one less distinct char
                if counts[char] == 0:
                    distincts -= 1

                left += 1

            # Expand window
            else:

                right += 1

                if right == len(s):
                    break

                newChar = s[right]

                # Increase count
                counts[newChar] = counts[newChar] + 1

                # If count went from 0 to 1, have new distinct char
                if counts[newChar] == 1:
                    distincts += 1

        return best


if __name__ == "__main__":
    # print(Solution().lengthOfLongestSubstringKDistinct("eceba", 2))
    print(Solution().lengthOfLongestSubstringKDistinct("abaccc", 2))