class Solution:

    def numDecodings(self, s: str) -> int:
        self.memo = {}
        if not input:
            return 0
        return self.recursiveWithMemo(0, s)

    def recursiveWithMemo(self, index: int, s: str) -> int:
        if index == len(s):
            return 1

        if s[index] == "0":
            return 0

        if index == len(s)-1:
            return 1

        if index in self.memo:
            return self.memo[index]

        ans = self.recursiveWithMemo(index+1, s) \
                + (self.recursiveWithMemo(index+2, s) if (int(s[index : index+2]) <= 26) else 0)

        self.memo[index] = ans

        return ans

                
if __name__ == "__main__":
    s = Solution()

    # print(s.numDecodings("1")) #1
    # print(s.numDecodings("26")) #2
    # print(s.numDecodings("11")) #2
    # print(s.numDecodings("111")) #3
    # print(s.numDecodings("112")) #3
    # print(s.numDecodings("27")) #1
    # print(s.numDecodings("01")) #0
    # print(s.numDecodings("0")) #0
    # print(s.numDecodings("10")) #1
    # print(s.numDecodings("9371597631128776948387197132267188677349946742344217846154932859125134924241649584251978418763151253")) #3981312