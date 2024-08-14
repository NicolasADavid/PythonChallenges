'''
❓ PROMPT
Define a subsequence of a string "s" to be a list of characters from "s" such that the characters appear in the same order in the list and in "s".

For instance, for the string "abcd", "a", "ab", and "acd" are valid subsequences, whereas "db" is not, since "b" comes before "d" in the original string.

Given an input string, return all subsequences except the empty string.

Example(s)
getAllSubsequences("abc") ==
  ["a", "b", "c", "ab", "ac", "bc", "abc"]
 

🔎 EXPLORE
List your assumptions & discoveries:

Options are each character in C.

Order matters. one char, to the full string are all options.

Choose 1,
Choose 2,
Choose 3,
Choose N

Make N choices. Include/Omit char at i.
For i in range(N):

for abcd:

""      -> a omit b omit c omit d omit
"abcd"  -> a incl b incl c incl d incl
"ad"    -> a incl b omit c omit d incl

Once n - 1 choices are made, answer constructed


Insightful & revealing test cases:

"a"
"abcd"
"aaa"
"1234"
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1:
Time: O(2^N) -> Make two choices for each char in input
Space: O(N) -> Create up to N stack frames.
Output: O(2^N) -> Large answer set
 

📆 PLAN
Outline of algorithm #: 

Recursive:

Given word, a subsequence to construct of word, and an index,
if subsequence is completed (index is at end of word(omit/select has happened for every character)), add answer
if subsequence not complete (index is at a char in word):
    two choices:
        add char at index to subsequence ++index, recurse
        omit char at index to subsequence ++index, recurse

return answer set
 


'''

# 🛠️ IMPLEMENT
# function getAllSubsequences(word) {
def getAllSubsequences(word: str) -> list[str]:

    answers = []

    def helper(word: str, subseq: str, i: int) -> None:
        # Ever character has been included or omitted
        if i == len(word):
            if len(subseq) > 0:
                answers.append(subseq)
            return
        
        # include character at i
        helper(word, subseq+word[i], i+1)

        # omit character at i
        helper(word, subseq, i+1)

    helper(word, "", 0)
    return answers
 

# 🧪 VERIFY
# Run tests. Methodically debug & analyze issues.

print(getAllSubsequences("abc"))
print(getAllSubsequences("aaa"))
print(getAllSubsequences("123"))
