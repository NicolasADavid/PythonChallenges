from typing import List
class Solution:
    def validWordSquare(self, words: List[str]) -> bool:
        n = len(words)

        for i in range(n):

            cw = []
            rw = []

            # Get column words
            # Get row words
            for j in range(len(words[i])):
                try:
                    cw.append(words[j][i])
                    rw.append(words[i][j])
                except Exception:
                    return False
            cw = "".join(cw)
            rw = "".join(rw)
            print("row word %s", rw)
            print("col word %s", cw)

            if cw != rw:
                return False
            
        return True
    

# print(Solution().validWordSquare(["abcd","bnrt","crmy","dtye"])) #True
# print(Solution().validWordSquare(["abcd","bnrt","crm","dt"])) #True
# print(Solution().validWordSquare(["ball","area","read","lady"])) #False
print(Solution().validWordSquare(["ball","asee","let","lep"])) #False




        