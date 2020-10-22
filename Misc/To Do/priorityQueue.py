import heapq

# l1 = [5, 1, 5, 6, 8, 2]

# print(l1)

# print("heapify")
# heapq.heapify(l1)

# print(l1)

# print("heappop")
# print(heapq.heappop(l1))

# print(l1)

# print("heappushpop")
# print(heapq.heappushpop(l1, 0))

# print(l1)


# heapq.heappush(l1, 0)
# heapq.heappush(l1, 10)
# heapq.heappush(l1, 11)

# print(l1)

# print("end")

# t1 = (1, "one")
# t2 = (2, "two")
# t3 = (3, "three")


# q = []

# heapq.heappush(q, t2)
# print(q)

# heapq.heappush(q, t1)
# print(q)

# heapq.heappush(q, t3)
# print(q)

# r = heapq.heappop(q)
# print(r)
# print(q)




class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


ln1 = ListNode(1)
ln2 = ListNode(2)
ln3 = ListNode(2)

q = []

# heapq.heappush(q, (ln1.val, ln1))
heapq.heappush(q, (ln1.val, ln1))
# heapq.heappush(q, (ln2.val, ln2))
heapq.heappush(q, (ln2.val, ln2))
# heapq.heappush(q, (ln3.val, ln3))
heapq.heappush(q, (ln3.val, ln3))
print(heapq.heappop(q))
print(heapq.heappop(q))
print(heapq.heappop(q))



# try:
#     import Queue as Q  # ver. < 3.0
# except ImportError:
#     import queue as Q

# q = Q.PriorityQueue()
# q.put(10)
# q.put(1)
# q.put(5)
# while not q.empty():
# 	print q.get(),