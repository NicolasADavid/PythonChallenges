from typing import List
from collections import defaultdict
class Solution:
    def areSentencesSimilar(self, sentence1: List[str], sentence2: List[str], similarPairs: List[List[str]]) -> bool:
        if len(sentence1) != len(sentence2):
            return False
        
        d = defaultdict(set)
        
        for pair in similarPairs:
            ss = d[pair[0]]
            ss.add(pair[1])

            ss = d[pair[1]]
            ss.add(pair[0])
        
        for i in range(len(sentence1)):
            word1 = sentence1[i]
            word2 = sentence2[i]

            if not (word1 == word2 or word1 in d[word2] or word2 in d[word1]):
                return False
            
        return True

print(Solution().areSentencesSimilar(["great","acting","skills"], ["fine","drama","talent"], [["great","fine"],["drama","acting"],["skills","talent"]]))
print(Solution().areSentencesSimilar(["great"], ["great"], []))
print(Solution().areSentencesSimilar(["great"], ["doubleplus", "great"], ["great", "doubleplus"]))