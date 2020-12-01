from typing import List

class Solution:
    def shortestDistance(self, words: List[str], word1: str, word2: str) -> int:
        
        word1Idx, word2Idx = None, None
        
        best = None

        for idx, word in enumerate(words):
            if word == word1:
                word1Idx = idx
            if word == word2:
                word2Idx = idx

            if word1Idx is not None and word2Idx is not None:
                distance = max(word1Idx, word2Idx) - min(word1Idx, word2Idx)
                best = min(best, distance) if best is not None else distance

        return best

if __name__ == "__main__":
    s = Solution()
    # v = s.shortestDistance(["practice", "makes", "perfect", "coding", "makes"], "coding", "practice")        
    # print(v)

    v = s.shortestDistance(["a","c","b","a"], "a", "b")
    print(v)
