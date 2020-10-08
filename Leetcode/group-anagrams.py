from typing import List

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


if __name__ == "__main__":
    s = Solution()
    print(s.groupAnagrams(["eat","tea","tan","ate","nat","bat"]))

            