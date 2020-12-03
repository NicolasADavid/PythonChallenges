class Solution:
    def longestValidParentheses(self, s: str) -> int:


        best = 0

        # Scan from left to right, then right to left
        # Count open + closed brackets found
        # When closed == open, validLength = closed * 2, track best
        # When closed > open, reset count of open + closed
        # Since we're waiting for closed to equal open before updating, scan ltr and rtl
        # in order to cover cases where open always > closed when scanning from ltr or rtl 


        # left to right

        opens = 0
        closed = 0
        for token in s:

            if token == '(': opens += 1

            if token == ')': closed += 1

            if closed > opens:
                opens = 0
                closed = 0

            if closed == opens:
                best = max(best, closed * 2)
                
        # right to left

        opens = 0
        closed = 0
        for token in reversed(s):

            if token == ')': opens += 1

            if token == '(': closed += 1

            if closed > opens:
                opens = 0
                closed = 0

            if closed == opens:
                best = max(best, closed * 2)

        return best
        
if __name__ == "__main__":
    s = Solution()
    print(s.longestValidParentheses("())(((((((((((((()))))"))  #10
    print(s.longestValidParentheses("())((())))"))  #6
    print(s.longestValidParentheses(")()())"))      #4
    print(s.longestValidParentheses("(()"))         #2
    print(s.longestValidParentheses("()"))          #2
    print(s.longestValidParentheses(""))            #0


    #     n = len(s)
        
    #     best = 0

    #     start = 0
    #     end = 0

    #     opens = []
    #     windowEnd = 0
    #     newWindowLen = 0

    #     while end < n - 1:

    #         nextChar = s[end+1]

    #         if nextChar is ')':
    #             # check if there is an open
    #             if len(opens):
    #                 # valid
    #                 # pop the open bracket
    #                 opens.pop()
    #                 # Add to newWindowLen
    #                 newWindowLen += 2
    #         if nextChar is '(':
    #             opens.append('(')

    #         # If all opens used, can add length of window
    #         if not len(opens):
    #             best += newWindowLen
    #             newWindowLen = 0
    #             windowEnd += newWindowLen

    #         # Does new character make the window's string valid or invalid?
    #         # Valid:
    #             # Add windowLength to best
    #             # Reset window
    #         # Invalid:
    #             # Move start to windowEnd+1
    #             # Reset window

    #     return best


            
    #     # move end until invalid or valid parentheses are found
    #     # if valid found, add to best
    #     # if invalid found: reset best, move start
    #     # if indeterminate, move windowEnd
            
            