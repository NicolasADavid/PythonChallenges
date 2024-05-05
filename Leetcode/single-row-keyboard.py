class Solution:
    def calculateTime(self, keyboard: str, word: str) -> int:
        
        idxs = {}

        for idx, c in enumerate(keyboard):
            idxs[c] = idx

        last = 0
        ans = 0

        for c in word:
            trgt = idxs[c]
            ans += abs(trgt - last)
            last = trgt

        return ans


        


Solution().calculateTime("abcdefghijklmnopqrstuvwxyz", "cba")