from sortedcontainers import SortedList, SortedDict, SortedSet

# SortedList
sl = SortedList([3, 1, 4, 1, 5, 9, 2, 6])
print(sl)
# Output: SortedList([1, 1, 2, 3, 4, 5, 6, 9])

sl.add(0)
print(sl)
# Output: SortedList([0, 1, 1, 2, 3, 4, 5, 6, 9])

# SortedDict
sd = SortedDict({'c': 3, 'a': 1, 'b': 2})
print(sd)
# Output: SortedDict({'a': 1, 'b': 2, 'c': 3})

# SortedSet
ss = SortedSet([3, 1, 4, 1, 5, 9, 2, 6])
print(ss)
# Output: SortedSet([1, 2, 3, 4, 5, 6, 9])