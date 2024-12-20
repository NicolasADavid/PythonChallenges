"""

Given a dictionary (represented by an array of string) and a word, return an array containing all words that can be created by adding one letter to the word.
 

EXAMPLE(S)
dictionary: `["ACT", "CAT", "CART", "ACTS", "BAT"]`
word: `"CAT"`
would return `["ACTS", "CART"]`

because these words can be formed with the letters "C", "A", "T", and exactly one more letter.
 

FUNCTION SIGNATURE
def possibleWords(dictionary, word):


Discoveries:
-All uppercase
-anagrams - order of characters
-Only consider words with length of original word + 1


Possible approaches:
- we will do frequency counter for each letter, we will have separate variable to count differences, add the word to result array if diffrences equals 1 

Has to be 4 long, 3 same letters
Dict of letter counts. Order does not matter.
Word is N+1 length

Create count from target word and N words in dictionary of L length (O(iL + N*L))
O(1)

Array vs hashmap

Possible approaches:
- Create letter counts in an a array or dictionary
- 

Anagram.. can sort the words. The order/sequence would be the same except for 1 character

"""


from collections import defaultdict

def possibleWords(dictionary, target):

    # counter for answers
    ans = []

    # count dict from target word
    targetCount = defaultdict(int)
    for c in target:
        targetCount[c] = targetCount[c] + 1
        
    # loop for each dictionary word
    for word in dictionary:
        # fail fast (check length)
        if len(word) != len(target) + 1:
            continue
        
        # count dict for the dictionary words
        dictCount = defaultdict(int)

        # Filling count dict from word
        for c in word:
            dictCount[c] = dictCount[c] + 1

        # Comparing to target word count dict
        is_valid = True
        diff = 0
        for key in dictCount.keys():

            remainder = dictCount[key] - targetCount[key]

            if remainder == 1:
                diff += 1
            elif remainder > 1 or remainder < 0:
                is_valid = False
                break

        if is_valid and diff == 1:
            ans.append(word)        

    return ans


dictionary = ["CAT", "CART", "ACTS", "BAT"]
word = "CAT"
print(possibleWords(dictionary, word)); # ["ACTS", "CART"]

dictionary = ["JOB", "BACKS", "LACKS", "RACKS"]
word = "BACK"
print(possibleWords(dictionary, word)); # ["BACKS"]
