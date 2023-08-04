import heapq
nums = [1, 2, 3, 4, 5]
hc = 0
h = []      # heap
# push the number into the heap
# negative so larger values of n are higher in the heap
# re-invert the number when taking out of the heap
for n in nums:
    heapq.heappush(h, -n)
    hc += 1

print("Numbers from highest value to lowest value: ")
while h:
    num = -heapq.heappop(h)
    print(num)
