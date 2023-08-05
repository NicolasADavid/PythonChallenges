class Solution:
    def isValid(self, s: str) -> bool:
        stack = []

        for c in s:
            if not stack:
                stack.append(c)
            else:
                top = stack[-1]
                
                if c == ")":
                    if top != "(":
                        return False
                    stack.pop()
                elif c == "]":
                    if top != "[":
                        return False
                    stack.pop()
                elif c == "}":
                    if top != "{":
                        return False
                    stack.pop()
                else:
                    stack.append(c)

        return not stack


# # Example 1:

# print(Solution().isValid("()"))

# # Example 2:

# print(Solution().isValid("()[]{}"))

# # Example 3:

# print(Solution().isValid("(]"))

print(Solution().isValid("{[]}"))