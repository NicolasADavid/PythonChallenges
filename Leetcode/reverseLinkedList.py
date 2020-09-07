# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:

        # store next node in tmp
        tmp = head.next

        # head will become tail of result and point to None 
        head.next = None

        # head is the last node processed
        last = head

        # while there is a next node in the original list
        while(tmp):
            # store tmp as the next node
            next = tmp

            #advance tmp to next's next
            tmp = next.next

            # point next's next to the last node
            next.next = last

            # next is the the new last node processed
            last = next
        
        return last
        

if __name__ == "__main__":

    s = Solution()

    l1 = ListNode(1, ListNode(2, ListNode(3)))

    r = s.reverseList(l1)

    while(r):
        print(r.val)
        r = r.next