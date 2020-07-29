class Solution:
    def isValid(self, s: str) -> bool:

        stack = []

        temp = {
            '(':')',
            '[':']',
            '{':'}'
        }

        # for each character
        for c in s:

            # if opening
            if(c in temp.keys()):
                stack.append(c)

            # if closing
            if(c in temp.values()):
                if not stack:
                    return False
                # if last token is not matching opening
                if c == temp[stack[len(stack)-1]]:
                    stack.pop()
                else:
                    # invalid
                    return False
        
        if not stack:
            return True
        else:
            return False

if __name__ == "__main__":

    s = Solution()

    print(s.isValid("(){}[]"))
    print(s.isValid("(){}["))
    print(s.isValid("(){][]"))
    print(s.isValid(""))
    print(s.isValid(""))
    print(s.isValid("(a){b}[a]"))
