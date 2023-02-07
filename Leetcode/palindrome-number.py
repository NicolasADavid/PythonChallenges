class Solution:
    def isPalindrome(self, x: int) -> bool:
        s = str(x)
        i = 0
        l = len(s) - 1

        while(i < l and i != l):
            if s[i] != s[l]:
                return False
            else:
                i += 1
                l -= 1

        return True


if __name__ == "__main__":
    print(Solution().isPalindrome(1221))