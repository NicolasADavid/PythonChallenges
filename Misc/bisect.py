from bisect import bisect, bisect_left, bisect_right


list = [1, 3, 5, 7, 10, 11, 16, 20]

s1 = 1
s2 = 3
s3 = 30

idx = bisect(list, s1)
print(idx)
idx = bisect_left(list, s1)
print(idx)
idx = bisect_right(list, s1)
print(idx)

print("---")

idx = bisect(list, s2)
print(idx)
idx = bisect_left(list, s2)
print(idx)
idx = bisect_right(list, s2)
print(idx)

print("---")

idx = bisect(list, s3)
print(idx)
idx = bisect_left(list, s3)
print(idx)
idx = bisect_right(list, s3)
print(idx)

print("---")
