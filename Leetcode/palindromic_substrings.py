"""
647. Palindromic Substrings

Given a string s, return the number of palindromic substrings in it.

A string is a palindrome when it reads the same backward as forward.

A substring is a contiguous sequence of characters within the string.

 

Example 1:

Input: s = "abc"
Output: 3
Explanation: Three palindromic strings: "a", "b", "c".
Example 2:

Input: s = "aaa"
Output: 6
Explanation: Six palindromic strings: "a", "a", "a", "aa", "aa", "aaa".
"""

class Solution:
    def countSubstrings(self, s: str) -> int:
        n = len(s)
        ans = 0
        for center in range(2*n - 1):

            left = center // 2
            right = left + center % 2

            # print("center", center)
            # print("left", left)
            # print("right", right)

            while left >= 0 and right < n and s[left] == s[right]:
                # print("shift")
                ans += 1
                left -= 1
                right += 1

            # print("-----")
        return ans
    
print(Solution().countSubstrings("abc"))  # Output: 3
print(Solution().countSubstrings("aaa"))  # Output: 6