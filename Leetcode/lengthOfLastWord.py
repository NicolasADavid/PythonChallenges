class Solution:

    @staticmethod
    def lengthOfLastWord(s: str) -> int:

        # if empty, return 0
        if (not s):
            return 0

        # get array of strings split on space
        words = s.split()

        #if empty, return 0
        if(len(words) == 0):
            return 0

        # last word
        word = words[-1] 

        length = len(word)

        # print(s)
        # print(length)
        return length

# if __name__ == "__main__":
    
#     Solution.lengthOfLastWord("Hello world")
#     Solution.lengthOfLastWord(" Hello world ")
#     Solution.lengthOfLastWord(" Hello world The a b b b b b b ")


