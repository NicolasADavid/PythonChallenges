from collections import deque
from typing import List

# def fullJustify(length: int, string: str) -> List[str]:
    
#     output = []
    
#     inputTokens = deque(string.split(" "))
    
#     for idx, token in enumerate(inputTokens):
#         token += " "
#         inputTokens[idx] = token
        
#     while inputTokens:
        
#         lineTokens = []
#         currLen = 0
        
#         # collect a token if adding new token len to currLen does not cause it to exceed target

#         # def lengthOfLineToBe():
#         #     if lineTokens:
#         #         implicitSpaces = len(lineTokens) - 1
#         #         return currLen + implicitSpaces
#         #     else:
#         #         return 0

#         # TODO: Prevent lines from ending with spaces
            
#         while inputTokens and currLen < length and len(inputTokens[0]) <= (length - currLen):
#         # while inputTokens and currLen < length and len(inputTokens[0]) <= (length - lengthOfLineToBe()):
#             nextToken = inputTokens.popleft()
#             currLen += len(nextToken)
#             lineTokens.append(nextToken)

#         # Add implicit spaces
#         # if lineTokens:
#         #     for i in range(len(lineTokens) - 1):
#         #         lineTokens[i] = lineTokens[i] + " "
        
#         if inputTokens:

#             if lineTokens:

#                 spacesToAdd = length - currLen

#                 if spacesToAdd > 0:

#                     if len(lineTokens) > 1:

#                         spacesToAddEvenly = spacesToAdd // (len(lineTokens) - 1)
#                         spacesRemaining = spacesToAdd % (len(lineTokens) - 1)

#                         # add spaces evenly
#                         for i in range(len(lineTokens) - 1):
#                             spaces = ""
#                             for j in range(spacesToAddEvenly):
#                                 spaces += " "
#                             lineTokens[i] += spaces

#                         # add remaining spaces
#                         for i in range(spacesRemaining):
#                             lineTokens[i] += " "
#                     else:
#                         for i in range(spacesToAdd):
#                             lineTokens[0] += " "
#             else:
#                 # Have to hyphenate
#                 hyphenateToken = inputTokens.popleft()
#                 keep = hyphenateToken[:length - 1] + "-"
#                 inputTokens.appendleft(hyphenateToken[length-1:])

#                 lineTokens.append(keep)
        
#         nextLine = "".join(lineTokens)
#         output.append(nextLine)
    
#     return output

class Solution:
    
    # def justify(length: int, string: str) -> List[str]:
            
    #     output = []
        
    #     inputTokens = deque(string.split(" "))
        
    #     # for idx, token in enumerate(inputTokens):
    #     #     token += " "
    #     #     inputTokens[idx] = token
            
    #     while inputTokens:
            
    #         lineTokens = []

    #         currLen = 0
            
    #         # collect a token if adding new token len to currLen does not cause it to exceed target

    #         def lengthOfLineToBe():
    #             if lineTokens:
    #                 implicitSpaces = len(lineTokens)
    #                 return currLen + implicitSpaces
    #             else:
    #                 return 0

    #         # while inputTokens and currLen < length and len(inputTokens[0]) <= (length - currLen):
    #         while inputTokens and currLen < length and len(inputTokens[0]) <= (length - lengthOfLineToBe()):
            
    #             nextToken = inputTokens.popleft()
    #             currLen += len(nextToken)
    #             lineTokens.append(nextToken)
            
    #         if inputTokens:

    #             if lineTokens:

    #                 spacesToAdd = length - currLen

    #                 if spacesToAdd > 0:

    #                     if len(lineTokens) > 1:

    #                         spacesToAddEvenly = spacesToAdd // (len(lineTokens) - 1)
    #                         spacesRemaining = spacesToAdd % (len(lineTokens) - 1)

    #                         # add spaces evenly
    #                         for i in range(len(lineTokens) - 1):
    #                             spaces = ""
    #                             for j in range(spacesToAddEvenly):
    #                                 spaces += " "
    #                             lineTokens[i] += spaces

    #                         # add remaining spaces
    #                         for i in range(spacesRemaining):
    #                             lineTokens[i] += " "
    #                     else:
    #                         for i in range(spacesToAdd):
    #                             lineTokens[0] += " "
    #             else:
    #                 # Have to hyphenate
    #                 hyphenateToken = inputTokens.popleft()
    #                 keep = hyphenateToken[:length - 1] + "-"
    #                 inputTokens.appendleft(hyphenateToken[length-1:])

    #                 lineTokens.append(keep)
    #         else:
    #             for i in range(len(lineTokens)):
    #                 lineTokens[i] += " "
            
    #         nextLine = "".join(lineTokens)
    #         output.append(nextLine)
        
    #     return output

    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
             
        output = []
        
        inputTokens = deque(words)
        
        while inputTokens:
            
            lineTokens = []

            currLen = 0
            
            # collect a token if adding new token len to currLen does not cause it to exceed target

            def lengthOfLineToBe():
                if lineTokens:
                    implicitSpaces = len(lineTokens)
                    return currLen + implicitSpaces
                else:
                    return 0

            while inputTokens and currLen < maxWidth and len(inputTokens[0]) <= (maxWidth - lengthOfLineToBe()):
            
                nextToken = inputTokens.popleft()
                currLen += len(nextToken)
                lineTokens.append(nextToken)
            
            if inputTokens:

                if lineTokens:

                    spacesToAdd = maxWidth - currLen

                    if spacesToAdd > 0:

                        if len(lineTokens) > 1:

                            spacesToAddEvenly = spacesToAdd // (len(lineTokens) - 1)
                            spacesRemaining = spacesToAdd % (len(lineTokens) - 1)

                            # add spaces evenly
                            for i in range(len(lineTokens) - 1):
                                spaces = ""
                                for j in range(spacesToAddEvenly):
                                    spaces += " "
                                lineTokens[i] += spaces

                            # add remaining spaces
                            for i in range(spacesRemaining):
                                lineTokens[i] += " "
                        else:
                            for i in range(spacesToAdd):
                                lineTokens[0] += " "
                else:
                    # Have to hyphenate
                    hyphenateToken = inputTokens.popleft()
                    keep = hyphenateToken[:maxWidth - 1] + "-"
                    inputTokens.appendleft(hyphenateToken[maxWidth-1:])

                    lineTokens.append(keep)
            else:
                for i in range(len(lineTokens) - 1):
                    lineTokens[i] += " "
                    currLen += 1

                diff = maxWidth - currLen
                for i in range(diff):
                    lineTokens[-1] += " "
            
            nextLine = "".join(lineTokens)
            output.append(nextLine)
        
        return output

        

if __name__ == "__main__":
    # input1 = "This is a long piece of text that should be justified. Please work. I really hope I wrote good code. I want to get hired. Please. I need to buy food for my pets.."
    # # input1 = "This is a piece of text with an incredibly long word: DO_NOT_MESS_WITH_ME_I_WILL_CRY that was a long word wow. wow. wow. wow."

    # r1 = Solution.justify(25, input1)
    # for line in r1:
    #     print(line)
    

    # in2 = "This is some sample text, really just enough to generate a few lines in the output to show what the text justify function is supposed to do."
    # r2 = Solution.justify(in2, 25)

    # for line in r2:
    #     print(line)

    # print("")


    in2 = "This is some sample text, really just enough to generate a few lines in the output to show what the text justify function is supposed to do."
    in2 = in2.split(" ")
    r2 = Solution().fullJustify(in2,  25)

    for line in r2:
        print(line)


    ["ask   not   what","your country can","do  for  you ask","what  you can do","for your country "]
    ["ask   not   what","your country can","do  for  you ask","what  you can do","for your country"]