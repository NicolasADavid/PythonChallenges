import math
# Add any extra import statements you may need here

from collections import defaultdict

# Add any helper functions you may need here

# two strings s and t, both of length N

# find maximum num of possible matching pairs in s and t after swapping exactly two characters within s

# swap s[i] and s[j] to maximize pairs (s[i] = t[i]) in s and t

# Must swap at different indices

# return int

# A swap may increase the number of matching pairs by 0, 1, or 2
# A swap may also decrease by 0, 1, or 2. We have to swap something.

# sliding window where best is num of pair increased

# maybe1
# increase right until best goes up
# risk overlooking best option
# this is not really a window, it's two points. Expanding and contracting a window considers all things in the window, we're only considering two indices

# maybe2
# create tuples of (s[i], t[i], i) for every position i where s[i] and t[i] differ.
# We really want two tuples where t1[0] = t2[1] and t1[1] = t2[0]
# For each tuple? (brutish)

# s = abcd
# t = adcb
# can get +2

# s = mna
# t = mbn
# can get +1

# s = aaa
# t = aaa
# can get +0

# s = mnb
# t = mna
# can get -1

# s = mno
# t = mno
# can get -2

# Tuple = (s[i], t[i], i)

# +2 if 1[0] == 2[1] and 1[1]   =     2[0]
# +1 if 1[0] == 2[1] and 1[1]   !=    2[0]
# +0 if 1[0] != 2[1] and 1[1]   !=    2[0]
# -1 if 1[0] == 2[0] 

# Create two lists, one sorted by t[0] and one sorted by [t1]
# One merge/pass of the lists could be used to determine what index i gains +1, 0, -1
# One merge/pass of the lists could be used to determine what index j gains +1, 0, -1

#   maybe3
#   Check every swap and see what the difference would be


# def matching_pairs(s, t):
#   # Write your code here
#   best = 0

#   for idx1, s1 in enumerate(s):

#       for idx2, s2 in enumerate(s):

#         t1 = t[idx1]
#         t2 = t[idx2]

#         gain = None

#         # s1 a  s2 b
#         # t1 b  t2 a

#         if s1 == t2 and s2 == t1 and s1 != s2 and t1 != t2:
#             gain = 2

#         # s1 a  s2 b
#         # t1 b  t2 a

#         if s1 == t2 and s2 == t1

#         #   +1
#         #   0
#         #   -1
#         #   -2


# def matching_pairs(s, t):

#     if s == t



# def matching_pairs(s, t):
#   if s == t:
#     return len(s) - 2
  
#   unmatched_pairs = set()
#   unmatched_in_t = set()
#   unmatched_in_s = set()
#   count = 0
#   found_perfect_swap = False
#   partial_swap = False

#   for i in range(len(s)):
#     if s[i] == t[i]:
#       count += 1
#     if found_perfect_swap:
#       # No need to keep looking for swaps
#       continue

#     if s[i] != t[i]:
#       unmatched_pairs.add((s[i], t[i]))
#       unmatched_in_t.add(t[i])
#       unmatched_in_s.add(s[i])
#       # If we found the inverse pair, perfect swap
#       if (t[i], s[i]) in unmatched_pairs:
#         found_perfect_swap = True
#       # Otherwise see if we have a "partial swap"
#       elif s[i] in unmatched_in_t or t[i] in unmatched_in_s:
#         partial_swap = True

#   if found_perfect_swap:
#     return count + 2
#   elif partial_swap:
#     return count + 1

# def matching_pairs(s, t):
#     seen = set()
#     hasDupe = False

#     res = 0

#     unmatchedS = []
#     unmatchedT = []

    
#     # Count matching pairs and collect not matching chars in s and t
#     for i in range(len(s)):

#         si = s[i]
#         ti = t[i]

#         if(si != ti):
#             unmatchedS.append(si)
#             unmatchedT.append(ti)
#         else:

#             # If the char of this matching pair has been seen before
#             if(si in seen):
#                 hasDupe = True

#             # Count the matching pair
#             res += 1
    
#     if not unmatchedS:

#         # Two matching pairs that are of the same character means we can swap them
#         # and leave the number of matches unaffected
#         if hasDupe:
#             return res
        
#         #Have to break two matches
#         return res - 2

#     mapS = defaultdict(lambda: -1)
#     mapT = defaultdict(lambda: -2)

#     for i in range(len(unmatchedS)):
#         si = unmatchedS[i]
#         ti = unmatchedT[i]

#         # If an unmatched character in t also exists unmatched in s, swapping them will gain 1 pair
#         if ti in mapS:
#             res += 1

#         if mapS[ti] == mapT[si]:
#             return res+1

#         mapS[si] = i
#         mapT[ti] = i
    
#     return res + (-1 if len(unmatchedS) == 1 else 0)

# def matching_pairs(s, t):

#     n = len(s)
#     unmatchedS = []
#     unmatchedT = []

#     for i in range(n):
#         si = s[i]
#         ti = t[i]

#         if si != ti:
#             unmatchedS.append(si)
#             unmatchedT.append(ti)

#     if not unmatchedT: return n - 2

#     res = n - len(unmatchedT)
#     contains = 0


#     for char in unmatchedT:
#         if char in unmatchedS:
#             contains += 1
#             if contains == 2: break

#     return res + contains

# Brute force
def matching_pairs(s, t):

    n = len(s)

    matches = 0
    best = -3

    for i in range(n):

        if s[i] == t[i]:
            matches += 1

        for j in range(i+1, n):
            
            change = 0

            s1 = s[i]
            t1 = t[i]

            s2 = s[j]
            t2 = t[j]

            if s1 == t1:
                change -= 1
            
            if s2 == t2:
                change -= 1

            if s1 == t2:
                change += 1

            if s2 == t1:
                change += 1

            best = max(best, change)

    return matches + best
            
            
# Next try:
# Go through each pair of letters
# Count matches. Count times a particular letter is matched.
# Collect pairs that are different and their indexes
# Collect letters that are unmatched in s and their indexes in a dict
# Collect letters that are unmatched in t and their indexes in a dict
# If no unmatched, see if there are two similar matches. (+0 swap, else -2 swap)
# If one unmatched, see if there are two similar matches. (+0 swap, else -1 swap)
# See if any pair unmatched exists inverted unmatched (x, y) & (y, x) (+2 swap)
# See if any unmatched letter in s exists unmatched in t (+1 swap)

    
# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printInteger(n):
  print('[', n, ']', sep='', end='')

test_case_number = 1

def check(expected, output):
  global test_case_number
  result = False
  if expected == output:
    result = True
  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, 'Test #', test_case_number, sep='')
  else:
    print(wrongTick, 'Test #', test_case_number, ': Expected ', sep='', end='')
    printInteger(expected)
    print(' Your output: ', end='')
    printInteger(output)
    print()
  test_case_number += 1

if __name__ == "__main__":
    s_1, t_1 = "abcde", "adcbe"
    expected_1 = 5
    output_1 = matching_pairs(s_1, t_1)
    check(expected_1, output_1)

    s_2, t_2 = "abcd", "abcd"
    expected_2 = 2
    output_2 = matching_pairs(s_2, t_2)
    check(expected_2, output_2)

    # Add your own test cases here

    s_3 = "abcdx"
    t_3 = "abxcc"
    expected_3 = 4
    output_3 = matching_pairs(s_3, t_3)
    check(expected_3, output_3)
    
    
    # s = abcd
    # t = adcb
    # can get +2

    # s = mna
    # t = mbn
    # can get +1

    # s = aaa
    # t = aaa
    # can get +0

    # s = mnb
    # t = mna
    # can get -1

    # s = mno
    # t = mno
    # can get -2
    