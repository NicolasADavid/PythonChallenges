class Solution:
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:

        if len(s1) + len(s2) != len(s3):
            return False
        
        dp = [[False] * (len(s2) + 1) for _ in range(len(s1) + 1)]

        for i in range(len(s1) + 1):
            for j in range(len(s2) + 1):

                # print("---")

                # def func1():
                #     return dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]
                
                # def func2():
                #     return dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]
                
                # def func3():
                #     return (
                #         (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
                #         (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
                #     )

                # k = i + j - 1

                # Empty string
                if i == 0 and j == 0:
                    dp[i][j] = True

                # No selections from first string
                elif i == 0:
                    dp[i][j] = dp[i][j - 1] and s2[j - 1] == s3[i + j - 1]

                # No selections from second string
                elif j == 0:
                    dp[i][j] = dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]

                # i + j characters taken from either s1 or s2
                # s3[i + j - 1] must match either s1[i-1] or s2[j-1]
                # If using s1[i-1], then dp[i-1][j] must be True
                # If using s2[j-1], then dp[i][j-1] must be True
                else:
                    dp[i][j] = (
                        (dp[i - 1][j] and s1[i - 1] == s3[i + j - 1]) or
                        (dp[i][j - 1] and s2[j - 1] == s3[i + j - 1])
                    )

        return dp[len(s1)][len(s2)]
    
if __name__ == "__main__":
    assert Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbcbcac")
    # assert Solution().isInterleave(s1="dbbca", s2="aabcc", s3="aadbbcbcac")
    assert not Solution().isInterleave(s1="aabcc", s2="dbbca", s3="aadbbbaccc")
    assert Solution().isInterleave(s1="", s2="", s3="")
    assert not Solution().isInterleave(s1="a", s2="", s3="b")
    assert not Solution().isInterleave(s1="", s2="b", s3="a")