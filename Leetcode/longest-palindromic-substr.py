class Solution:
    def longestPalindromeDP(self, s: str) -> str:
        n = len(s)
        dp = [[False] * n for _ in range(n)]
        ans = [0, 0]

        for i in range(n):
            dp[i][i] = True

        for i in range(n - 1):
            if s[i] == s[i + 1]:
                dp[i][i + 1] = True
                ans = [i, i + 1]

        for diff in range(2, n):
            for i in range(n - diff):
                j = i + diff
                if s[i] == s[j] and dp[i + 1][j - 1]:
                    dp[i][j] = True
                    ans = [i, j]

        i, j = ans
        return s[i : j + 1]
    
    def longestPalindrome(self, s):
    
        def check(i, j):
            left = i
            right = j - 1
            
            while left < right:
                if s[left] != s[right]:
                    return False
                
                left += 1
                right -= 1
                
            return True
        
        n = len(s)
        
        for end in range(n, 0, -1):
            for start in range(n - end + 1):
                if check(start, start+end):
                    return s[start : start + end]
                    
        return ""
                

print(Solution().longestPalindrome("babad"))