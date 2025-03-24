'''
Given three distinct words, determine if the third word is potentially a portmanteau of the first two.

A portmanteau (https://en.wikipedia.org/wiki/Portmanteau) is a word that is made by taking the start of one word and the end of another and mashing them together.
Brunch is a great example, combining the first 2 letters of "breakfast" with the last 4 of "lunch".

Compound words aren't considered portmanteaus, so "football" is not a portmanteau of "foot" and "ball". At least one of the two words needs to be truncated.
 

EXAMPLE(S)
isPortmanteau("smoke", "fog", "smog") == True (sm + og)
isPortmanteau("snake", "fog", "smog") == False
isPortmanteau("lunch", "breakfast", "brunch") == True (br + unch)
isPortmanteau("shrink", "inflation", "shrinkflation") == True (shrink + flation)
isPortmanteau("foot", "ball", "football") == False
 

FUNCTION SIGNATURE
function isPortmanteau(word1, word2, proposed) {
def isPortmanteau(word1: str, word2: str, proposed: str) -> bool:
'''

def isPortmanteau(word1: str, word2: str, proposed: str) -> bool:

    # rule out edge cases
    # compound words and exact matches
    if proposed == word1 or proposed == word2:
        return False
    if proposed == word1 + word2 or proposed == word2 + word1:
        return False
    
    def checkWords(word1, word2):

        p1 = 0

        # find the common prefix of word1 and proposed
        while p1 < len(word1) and p1 < len(proposed) and word1[p1] == proposed[p1]:
            p1 += 1

        p2 = len(word2) - 1
        t2 = len(proposed) - 1

        while p2 > 0 and t2 > 0 and word2[p2] == proposed[t2]:
            p2 -= 1
            t2 -= 1

        w1PrefixLength = p1
        w2SuffixLength = len(word2) - p2 - 1

        # if either prefix of word1 or suffix of word2 are empty
        if w1PrefixLength == 0 or w2SuffixLength == 0:
            return False
        
        # if the length of the prefix of word1 plus the length of the suffix of word2 is equal to or greater than the length of the proposed word
        if w1PrefixLength + w2SuffixLength >= len(proposed):
            return True
        
        return False
    
    return checkWords(word1, word2) or checkWords(word2, word1)

print("Tests")
assert isPortmanteau("fog", "smoke", "smog") == True
assert isPortmanteau("smoke", "fog", "smog") == True
assert isPortmanteau("motor", "hotel", "motel") == True
assert isPortmanteau("branch", "much", "brunch") == False
assert isPortmanteau("shrink", "inflation", "shrinkflation") == True
assert isPortmanteau("skimp", "inflation", "skimpflation") == True
assert isPortmanteau("miserable", "flimsy", "mimsy") == True
assert isPortmanteau("puppies", "cat", "puppi") == False
assert isPortmanteau("cat", "dog", "otter") == False
assert isPortmanteau("ten", "at", "tent") == True
assert isPortmanteau("at", "ten", "tent") == True
# special cases
# proposed is one of the words
assert isPortmanteau("bartender", "ten", "bartender") == False
assert isPortmanteau("bartender", "tender", "bartender") == False
assert isPortmanteau("bartender", "tenderness", "bartender") == False
# compounds aren't portmanteaus
assert isPortmanteau("foot", "ball", "football") == False
assert isPortmanteau("ski", "water", "waterski") == False
assert isPortmanteau("bat", "man", "batman") == False
assert isPortmanteau("man", "bat", "batman") == False
assert isPortmanteau("rent", "tent", "tent") == False
assert isPortmanteau("rent", "tent", "rent") == False
assert isPortmanteau("", "test", "test") == False
assert isPortmanteau("test", "", "test") == False
assert isPortmanteau("test", "test", "test") == False
assert isPortmanteau("", "", "test") == False
assert isPortmanteau("", "", "") == False