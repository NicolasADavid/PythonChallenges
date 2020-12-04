from typing import List

class Solution:
    def isAlienSorted(self, words: List[str], order: str) -> bool:

        map = {}

        for idx, letter in enumerate(order):
            map[letter] = idx

        lastWord = None

        for word in words:

            # first word is in order
            if not lastWord:
                lastWord = word
                continue

            # compare word and lastWord

            # from 0 to length of shortest word
            for i in range(0, min(len(lastWord), len(word))):
                # find a difference between the words
                if lastWord[i] != word[i]:
                    # compare map value of the letters that differ
                    if map[lastWord[i]] > map[word[i]]:
                        return False
                    # comparison was possible, break out of for loop
                    break
            else:
                # if comparison was not possible, lastWord should be of equal or shorter length compared to word
                return len(lastWord) <= len(word)

            # update lastWord
            lastWord = word

        return True

            
if __name__ == "__main__":
    s = Solution()
    s.isAlienSorted(["zirqhpfscx","zrmvtxgelh","vokopzrtc","nugfyso","rzdmvyf","vhvqzkfqis","dvbkppw","ttfwryy","dodpbbkp","akycwwcdog"], "khjzlicrmunogwbpqdetasyfvx")    
