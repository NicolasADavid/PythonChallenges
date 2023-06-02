# SoFi tech screen 2023

'''
You are given a string s and an integer k. You can choose any character of the string and change it to any other uppercase English character. You can perform this operation at most k times.

Return the length of the longest substring containing the same letter you can get after performing the above operations.

Example 1:

Input: s = "ABAB", k = 2
Output: 4
Explanation: Replace the two 'A's with two 'B's or vice versa.

Example 2:

Input: s = "AABABBA", k = 1
Output: 4
Explanation: Replace the one 'A' in the middle with 'B' and form "AABBBBA".
The substring "BBBB" has the longest repeating letters, which is 4.
There may exists other ways to achive this answer too.
'''

from collections import defaultdict


def longestSubstringWithSubstitutions(s: str, k: int):

    if not s:
        return 0

    r = 0
    l = 0
    best = 0

    substitutions = 0
    letter = s[l]

    # track counts of letters seen
    counts = defaultdict(int)
    counts[letter] = 1

    while r < len(s):
        # check solutions
        if substitutions <= k:
            best = max(best, r - l + 1)
            # expand
            r += 1
            if r == len(s):
                break
            counts[s[r]] = counts[s[r]] + 1
            if s[r] != letter:
                substitutions += 1
        else:
            # contract
            remove = s[l]
            counts[remove] = counts[remove] - 1
            l += 1

            # find largest count value in counts dictionary. Corresponding key is next target letter, minimizing need for substitutions.
            letter = max(counts, key=counts.get)
            lettercount = counts[letter]
            # sorted_keys_by_count = sorted(
            #     counts.items(), key=lambda x: x[1], reverse=True)
            # letter = sorted_keys_by_count[0][0]

            # How many substitutions must be made? Sum counts of other letters. That is new substitutions count.
            # otherLetterCountsSum = 0
            # for kv in sorted_keys_by_count[1:]:
            #     otherLetterCountsSum += kv[1]
            otherLetterCountsSum = sum(counts.values()) - lettercount

            substitutions = otherLetterCountsSum

    return best


def check(result: str, expected: int):
    if result == expected:
        print("pass")
    else:
        print("fail")
        print("expected: ", expected, " result: ", result)


expect = 4
result = longestSubstringWithSubstitutions("ABAB", 2)
check(result, expect)

expect = 4
result = longestSubstringWithSubstitutions("AABABBA", 1)
check(result, expect)

expect = 2
result = longestSubstringWithSubstitutions("AABABBA", 0)
check(result, expect)

expect = 10
result = longestSubstringWithSubstitutions("AABACAABBA", 4)
check(result, expect)

expect = 10
result = longestSubstringWithSubstitutions("AABACAABBA", 10)
check(result, expect)
