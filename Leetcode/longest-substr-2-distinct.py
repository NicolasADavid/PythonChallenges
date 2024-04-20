from collections import defaultdict
class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:

        k = 2
        b = 0
        n = len(s)

        left = 0
        right = 0

        d = defaultdict(int)

        d[s[right]] += 1

        def countdistinct():
            # return sum(1 if d[key] > 0 for key in d.keys())
            # At most 25 entries, O(25)
            return sum(1 for v in d.values() if v > 0)
        
        while right < n:
            if countdistinct() <= k:
                #track
                b = max(b, right - left + 1)

                #expand
                right += 1

                if right == n:
                    break
                else:
                    #incr count for element added to window dict
                    d[s[right]] += 1
            else:
                #decr count for element to be removed from window
                d[s[left]] -= 1
                #contract
                left += 1
        
        return b
            
if __name__ == "__main__":
    print(Solution().lengthOfLongestSubstringTwoDistinct(s = "ccaabbb"))