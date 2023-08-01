from typing import List
import collections

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        anagrams = {}

        for word in strs:

            letterSetMap = {}

            # construct letterSetMap
            for letter in word:
                curr = letterSetMap.setdefault(letter, 0)
                letterSetMap[letter] = curr + 1

            # create letterSet
            letterSet = tuple(sorted(letterSetMap.items()))

            if letterSet in anagrams:
                anagrams[letterSet].append(word)
            else:
                anagrams[letterSet] = [word]

        return anagrams.values()

# Way simpler editorial solution:
# class Solution(object):
#     def groupAnagrams(self, strs):
#         ans = collections.defaultdict(list)
#         for s in strs:
#             ans[tuple(sorted(s))].append(s)
#         return ans.values()

if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

            