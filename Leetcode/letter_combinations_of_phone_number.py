"""
17. Letter Combinations of a Phone Number
Medium
Topics
Companies
Given a string containing digits from 2-9 inclusive, return all possible letter combinations that the number could represent. Return the answer in any order.

A mapping of digits to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.


 

Example 1:

Input: digits = "23"
Output: ["ad","ae","af","bd","be","bf","cd","ce","cf"]
Example 2:

Input: digits = ""
Output: []
Example 3:

Input: digits = "2"
Output: ["a","b","c"]
 

Constraints:

0 <= digits.length <= 4
digits[i] is a digit in the range ['2', '9'].

"""

"""
Algorithm:
1. Create a mapping of digits to letters.
2. Initialize a list to store the combinations.
3. Define a recursive function to generate combinations.
4. Iterate through the digits and for each digit, iterate through its corresponding letters.
5. For each letter, append it to the current combination and call the recursive function with the next digit.
"""

class Solution(object):
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """

        m = {
            '2': 'abc',
            '3': 'def',
            '4': 'ghi',
            '5': 'jkl',
            '6': 'mno',
            '7': 'pqrs',
            '8': 'tuv',
            '9': 'wxyz'
        }

        res = []

        if not digits:
            return res
        
        def backtrack(combination, next_digits):
            if len(next_digits) == 0:
                res.append(combination)
            else:
                for letter in m[next_digits[0]]:
                    backtrack(combination + letter, next_digits[1:])

        backtrack("", digits)
        
        return res
        