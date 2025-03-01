from collections.abc import Iterator

class hn_wrapper(Iterator):
    def __init__(self, it):
        self.it = iter(it)
        self._hasnext = None
    def __iter__(self): 
        return self
    def __next__(self):
        if self._hasnext:
            result = self._thenext
        else:
            result = next(self.it)
        self._hasnext = None
        return result
    def hasnext(self):
        if self._hasnext is None:
            try: 
                self._thenext = next(self.it)
            except StopIteration: 
                self._hasnext = False
            else:
                self._hasnext = True
        return self._hasnext


numList = [x for x in range(4)]

numIter = iter(numList)



print()
print(next(numIter, "Bones"))
print(next(numIter, "Bones"))
print(next(numIter, "Bones"))
print(next(numIter, "Bones"))
print(next(numIter, "Bones"))


num_hn_iterator = hn_wrapper(iter(numList))

while num_hn_iterator.hasnext():
    print(num_hn_iterator.__next__())
else:
    print("Bones")

