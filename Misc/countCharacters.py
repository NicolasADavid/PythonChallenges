from typing import Counter

class Solution:
    def getMostCommon(self, input):

        if not input:
            return None
        
        cnt = Counter()
        for char in input:
            cnt[char] += 1

        return cnt.most_common(1)[0][0]

if __name__ == "__main__":
    s = Solution()
    print(s.getMostCommon("aab"))