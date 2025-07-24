'''
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


FUNCTION SIGNATURE
func minDistance(str1: String, str2: String) -> Int
'''
from functools import lru_cache
def min_distance(str1, str2):
    @lru_cache
    def helper(i, j):
        if i < 0:
            return j + 1
        if j < 0:
            return i + 1

        if str1[i] == str2[j]:
            return helper(i - 1, j - 1)
        else:
            return min(helper(i - 1, j), helper(i, j - 1), helper(i - 1, j - 1)) + 1

    return helper(len(str1) - 1, len(str2) - 1)

# print(min_distance("abcd", "abcde"))
# print(min_distance("abd", "abce"))

def min_distance_dp(str1, str2):

    n = len(str1)
    m = len(str2)

    dp = [[0 for _ in range(m) ] for _ in range(n) ]

    def print_arr():
        print("----")
        for row in dp:
            print(row)

    # # Fill first row
    # for i in range(m):
    #     dp[0][i] = i
    # # Fill first col
    # for i in range(n):
    #     dp[i][0] = i
    

    for i in range(n):
        for j in range(m):

            if i == 0:
                dp[i][j] = j
            if j == 0:
                dp[i][j] = i
                
            # Char match
            if str1[i] == str2[j]:
                dp[i][j] = dp[i-1][j-1]
            else:
                dp[i][j] = min(
                    dp[i-1][j],
                    dp[i][j-1],
                    dp[i-1][j-1]
                    ) + 1

    print_arr()
    return dp[n-1][m-1]

# print(min_distance_dp("abcd", "abcde"))
# print(min_distance_dp("abd", "abce"))

print(min_distance_dp("horse", "ros"))