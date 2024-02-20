class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        i = 0
        j = 0

        while i < len(s) and j < len(t):
            if s[i] == t[j]:
                i += 1
            j += 1

        return i == len(s)
    
if __name__ == "__main__":

    s = Solution()

    print(s.isSubsequence(s = "abc", t = "ahbgdc"))
    print(s.isSubsequence(s = "axc", t = "ahbgdc"))