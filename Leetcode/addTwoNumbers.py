# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        
        dummyHead = ListNode()
        tail = dummyHead
        carry = False

        while(l1 or l2):
            sum = 0

            #sum element from l1
            if(l1):
                # Sum and advance
                sum += l1.val
                l1 = l1.next

            #sum element from l2
            if(l2):
                # Sum and advance
                sum += l2.val
                l2 = l2.next

            #sum carry
            if(carry):
                sum += 1

            #reset carry
            carry = False
            
            #set carry
            if(sum > 9):
                sum = sum % 10
                carry = True

            #Append to list
            tail.next = ListNode(sum)
            tail = tail.next
            
        #if carry still true, add one more
        if carry:
            tail.next = ListNode(1)

        return dummyHead.next


if __name__ == "__main__":
    solution = Solution()

    l1 = ListNode(2, ListNode(4, ListNode(3)))
    l2 = ListNode(5, ListNode(6, ListNode(4)))
    
    solution.addTwoNumbers(l1, l2)