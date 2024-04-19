class Solution:
    def confusingNumber(self, n: int) -> bool:

        # same = [str(_) for _ in [0, 1, 8]]
        invalid = [str(_) for _ in [2, 3, 4, 5, 7]]
        flip = [str(_) for _ in [6, 9]]

        newdigitstring = []

        for digit in str(n):

            if digit in invalid:
                return False
            
            if digit in flip:

                if digit == "6":
                    newdigitstring.append("9")
                elif digit == "9":
                    newdigitstring.append("6")

            else:
                newdigitstring.append(digit)

        newdigitstring.reverse()
            
        if int("".join((newdigitstring))) == n:
            return False
        
        return True

if __name__ == "__main__":
    print(Solution().confusingNumber(6))
    print(Solution().confusingNumber(89))
    print(Solution().confusingNumber(11))
    print(Solution().confusingNumber(24102))

