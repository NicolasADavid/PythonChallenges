# class Solution:
    # def isPalindrome(self, x: int) -> bool:
    #     s = str(x)
    #     i = 0
    #     l = len(s) - 1

    #     while(i < l and i != l):
    #         if s[i] != s[l]:
    #             return False
    #         else:
    #             i += 1
    #             l -= 1

    #     return True

class Solution:
    def isPalindrome(self, x: int) -> bool:

        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        
        reverted = 0

        while x > reverted:
            reverted = reverted * 10 + x % 10
            x = x // 10
        
        if x == reverted or x == reverted // 10:
            return True
        else:
            return False
        
if __name__ == "__main__":
    print(Solution().isPalindrome(0))
    print(Solution().isPalindrome(1221))
    print(Solution().isPalindrome(12321))
    print(Solution().isPalindrome(123213))
    print(Solution().isPalindrome(10))
    print(Solution().isPalindrome(-121))