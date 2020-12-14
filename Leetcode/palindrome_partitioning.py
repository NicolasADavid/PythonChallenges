from typing import List
class Solution:

    def __init__(self):
        self.palindromeChecked = {}

    def checkPalindrome(self, s):

        if len(s) == 1:
            return True

        l, r = 0, len(s)-1

        while l <= r:
            if s[l] != s[r]:
                return False
            l += 1
            r -= 1
        else:
            return True

    def isPalindrome(self, s):

        # Have answer?
        if s in self.palindromeChecked:
            return self.palindromeChecked[s]
        
        # Check if is palindrome
        res = self.checkPalindrome(s)
        self.palindromeChecked[s] = res
        return res

    def helper(self, s: str, idx: int, lastSplit: int, solution: List[str], ans: List[List[str]]) -> None:
        
        # Have reached the end of the string
        if idx == len(s):

            # check if all substr are palindromes
            for substr in solution:
                if not self.isPalindrome(substr):
                    return

            # if valid, add to ans
            ans.append(solution)
            return


        # If only one char left, split decision already made
        if len(s) - idx == 1:
            # Split at this point
            ns = solution.copy()
            ns.append(s[lastSplit:idx+1])
            self.helper(s = s, idx = idx+1, lastSplit = idx+1, solution = ns, ans = ans)
        else:
            # Split at this point
            ns = solution.copy()
            ns.append(s[lastSplit:idx+1])
            self.helper(s = s, idx = idx+1, lastSplit = idx+1, solution = ns, ans = ans)
            
            # Don't split at this point
            self.helper(s = s, idx = idx+1, lastSplit = lastSplit, solution = solution, ans = ans)

        return ans

    def partition(self, s: str) -> List[List[str]]:

        partitions = self.helper(s, 0, 0, [], [])
        return partitions

if __name__ == "__main__":
    # print(Solution().partition("aab"))
    print(Solution().partition("aabbz"))
    # print(Solution().partition("aabb"))