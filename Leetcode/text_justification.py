'''
You are given an array of words (strings) and an integer maxWidth that represents the desired width of each line.

Task: Arrange the words so that each line has exactly maxWidth characters and is fully (left & right) justified.

Rules:
1. Pack as many words as possible into each line without exceeding maxWidth.
2. A single space must separate consecutive words on a line.
3. Extra spaces that remain after the mandatory single spaces should be distributed as evenly as possible from left to right between the gaps of the line. If there are more extra spaces than gaps, put one additional space in the left-most gaps first.
4. Lines that contain only one word should be left-justified (word followed by spaces).
5. The last line of the text should be left-justified and spaces should be added to the right to reach maxWidth.

Return the list of justified lines (each line represented as a string).
 

EXAMPLE(S)
Input: words = ["This","is","an","example","of","text","justification."], maxWidth = 16
Output:
[
 "This    is    an",
 "example  of text",
 "justification.  "
]

Input: words = ["What","must","be","acknowledgment","shall","be"], maxWidth = 16
Output:
[
 "What   must   be",
 "acknowledgment  ",
 "shall be        "
]
 

FUNCTION SIGNATURE
function fullJustify(words, maxWidth) {}
def full_justify(words: List[str], maxWidth: int) -> List[str]:


while words remain
  build list of words for a new line
  maintain count/length of new line
  while count/lenght + 1 * num_words + len(next word) < maxWidth:
    add word
  else
    justify the line
    while line length < maxWidth
      if only one word, add enough spaces directly (maxWidth - len(one_word))
      add space to end of word from left to right except last word
      if line length equals maxWidth, continue
'''

from collections import deque
from typing import List

class Solution(object):
    # def fullJustify(self, words, maxWidth):
    #     """
    #     :type words: List[str]
    #     :type maxWidth: int
    #     :rtype: List[str]
    #     """
        

    # def full_justify(self, words: List[str], maxWidth: int) -> List[str]:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:

        words = deque(words)

        answer = []

        while words:
            
            next_line_words = []
            next_line_words_char_count = 0

            while words and len(words[0]) + (next_line_words_char_count + len(next_line_words)) <= maxWidth:
                next_word = words.popleft()
                next_line_words_char_count += len(next_word)
                next_line_words.append(next_word)

                next_space_index = 0

            if words:
                if len(next_line_words) == 1:
                    answer.append(next_line_words[0] + (" " * (maxWidth - len(next_line_words[0]))))
                    continue
                while (next_line_words_char_count < maxWidth):
                    if next_space_index == len(next_line_words) - 1:
                        next_space_index = 0
                    else:
                        next_line_words[next_space_index] += " "
                        next_line_words_char_count += 1
                        next_space_index += 1
            else:

                # add a space after every word except the last one
                for i in range(0, len(next_line_words) - 1):
                    next_line_words[i] += " "
                    next_line_words_char_count += 1

                # add remaining spaces to final word
                while next_line_words_char_count < maxWidth:
                    next_line_words[-1] += " "
                    next_line_words_char_count += 1
                
            answer.append("".join(next_line_words))

        return answer



def arrays_equal(a: List[str], b: List[str]) -> bool:
    return a == b

print(arrays_equal(
    Solution().fullJustify(['This','is','an','example','of','text','justification.'],16),
    ['This    is    an','example  of text','justification.  ']))

print(arrays_equal(
    Solution().fullJustify(['What','must','be','acknowledgment','shall','be'],16),
    ['What   must   be','acknowledgment  ','shall be        ']))

print(arrays_equal(
    Solution().fullJustify(['Listen','to','many,','speak','to','a','few.'],6),
    ['Listen','to    ', 'many, ','speak ', 'to   a', 'few.  ']))