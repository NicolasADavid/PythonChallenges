"""
Levenshtein Distance

Given two strings, return the minimum number of changes to change the first string into the second string. A change can either be the insertion, deletion or substitution of a character.

Solve this problem on LeetCode:
https://leetcode.com/problems/edit-distance/


EXAMPLE(S)
"abcd", "abcde" => 1 (add 'e')
"abd", "abce" => 2 ("change 'd' to 'c', add 'e')

Diff: 1
ab
abc


Diff: 1
abdce
abdc

Recursive

given str1 and str2

Considering last character

if same
    recurse, move both indexes, no counting

if different

    min(insertion, deletion, substitution) + 1

    Insertion/Deletion
    - delete from first string
    Deletion
    - delete from second
    substitution
    - delete from both

Bottom-up

n x m matrix
dp[0][0] = 0, meaning no changes needed to convert an empty string to another empty string

dp[i][0] = i, meaning i changes needed to convert first i characters of str1 to an empty string
dp[0][j] = j, meaning j changes needed to convert an empty string to the first j characters of str2


FUNCTION SIGNATURE
func minDistance(str1: String, str2: String) -> Int
"""

from functools import lru_cache


def min_distance_recursive(str1, str2):
    @lru_cache
    def helper(i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if str1[i] == str2[j]:
            return helper(i - 1, j - 1)
        else:
            return (
                min(helper(i - 1, j), helper(i, j - 1), helper(i - 1, j - 1))
                + 1
            )

    return helper(len(str1) - 1, len(str2) - 1)


def min_distance_dp(str1, str2):
    n = len(str1)
    m = len(str2)

    if n == 0:
        return m

    if m == 0:
        return n

    dp = [[0 for _ in range(m + 1)] for _ in range(n + 1)]

    def print_arr():
        print("----")
        for row in dp:
            print(row)
        print("----")

    # Fill first row
    for i in range(1, n + 1):
        dp[i][0] = i

    # Fill first col
    for i in range(1, m + 1):
        dp[0][i] = i

    # print("initial dp:")
    # print_arr()

    for idx1 in range(1, n + 1):
        for idx2 in range(1, m + 1):
            # Char match
            if str1[idx1 - 1] == str2[idx2 - 1]:
                dp[idx1][idx2] = dp[idx1 - 1][idx2 - 1]
            else:
                dp[idx1][idx2] = (
                    min(
                        dp[idx1 - 1][idx2],  # Deletion from str1
                        dp[idx1][idx2 - 1],  # Deletion from str2
                        dp[idx1 - 1][idx2 - 1],  # Substitution
                    )
                    + 1 # Increment for the change (deletion or substitution)
                )
            # print("After processing", str1[:idx1], "and", str2[:idx2])
            # print_arr()

    print("Final dp:")
    print_arr()
    return dp[n][m]



word1 = "intention"
word2 = "execution"

print(min_distance_dp(word1, word2) == 5)
print(min_distance_recursive(word1, word2) == 5)
