class Solution(object):
    def removeStars(self, s):
        """
        :type s: str
        :rtype: str
        """
        
        stack = []

        for char in s:
            if char == "*":
                if stack:
                    stack.pop()
            else:
                stack.append(char)

        return "".join(stack)
    

assert Solution().removeStars("ab**c") == "c"
assert Solution().removeStars("leet**cod*e") == "lecoe"
assert Solution().removeStars("erase*****") == ""