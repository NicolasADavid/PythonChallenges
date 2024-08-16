'''
Given a set of characters, a minimum length, and a maximum length, generate all strings that can be created using characters from the set between those lengths inclusively.

This algorithm requires a large time and space complexity to enumerate all the possibilities. You should be able to get this to either time out or run out of memory even on rather small lengths. Try it! It's a fun demonstration of the exponential nature of some decision trees.
 

EXAMPLE(S)
generatePasswords(["a"], 2, 4) == [
  "aa",
  "aaa",
  "aaaa",
]

generatePasswords(["a", "b", "c"], 2, 3) == [
  "aa","aaa","aab","aac",
  "ab","aba","abb","abc",
  "ac","aca","acb","acc",
  "ba","baa","bab","bac",
  "bb","bba","bbb","bbc",
  "bc","bca","bcb","bcc",
  "ca","caa","cab","cac",
  "cb","cba","cbb","cbc",
  "cc","cca","ccb","ccc"
]
 

FUNCTION SIGNATURE
function generatePasswords(validCharacters, minLength, maxLength) {
def generatePasswords(validCharacters: list[str], minLength: int, maxLength: int) -> list[str]:
'''


def generatePasswords(validCharacters, minLength, maxLength):

    answers = []

    def helper(choices):

        nonlocal answers

        # Is build valid
        if len(choices) >= minLength and len(choices) <= maxLength:
            answers.append("".join(choices))

        # Is build at max
        if len(choices) == maxLength:
            return
        
        # Choose every option
        # N-ary decision tree. Can always use every character, no matter where we are in decision tree.
        for option in validCharacters:
            choices.append(option)
            helper(choices)
            choices.pop()
        
    helper([])

    return answers


print(generatePasswords(["a","b","c"], 2, 3))
o1 = generatePasswords(["a","b","c"], 2, 3)
e1 = set([
  "aa","aaa","aab","aac",
  "ab","aba","abb","abc",
  "ac","aca","acb","acc",
  "ba","baa","bab","bac",
  "bb","bba","bbb","bbc",
  "bc","bca","bcb","bcc",
  "ca","caa","cab","cac",
  "cb","cba","cbb","cbc",
  "cc","cca","ccb","ccc"
])

assert set(o1) == e1