from typing import List
class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """

        l = 0
        r = len(s) - 1

        while l < r:
            lc = s[l]
            rc = s[r]

            #swap
            s[l] = rc
            s[r] = lc

            #slide
            l += 1
            r -= 1

        return
        
if __name__ == "__main__":

    sol = Solution()

    s = ["h","e","l","l","o"]
    sol.reverseString(s)
    print(s)
    
    s = ["H","a","n","n","a","h"]
    sol.reverseString(s)
    print(s)
