'''
❓ PROMPT
Given a linked list and a target k, return a linked list containing every kth element.

Example(s)
head = 1 -> 3 -> 6 -> 2 -> 8 -> 9
everyKthNode(head, 3) == "6 -> 9"
 

🔎 EXPLORE
List your assumptions & discoveries:

Return a new list with the desired elements.

Have to read through the whole input.

Could potentiall do O(1) space if removing from the input rather than creating a new list.
 

Insightful & revealing test cases:

Empty list.
K = 1.
List with not exactly a multiple of k elements
 

🧠 BRAINSTORM
What approaches could work?
Algorithm 1: create new list from kth elements
Time: O(N)
Space: O(N)

Algorithm 2: Remove elements from list that are not the kth elements
Time: O(N)
Space: O(1)
 

📆 PLAN
Outline of algorithm #1:

start counter at 1 and pointer at first element
traverse list, increading counter. When count == k, put that element into new list
continue until input list traversed

Outline of algorithm #2:
Start counter 

 

🛠️ IMPLEMENT
function everyKthNode(node, target) {
def everyKthNode(node: Node, target: int) -> Node:
 

🧪 VERIFY
Run tests. Methodically debug & analyze issues.

'''


class ListNode():
    def __init__(self, value = None, next = None):
        self.value = value
        self.next = next

def everyKthNode(head: ListNode, k: int) -> ListNode:

    if k == 1:
        return head
    
    count = 1
    start = None
    last = None

    curr = head

    while curr:

        # At node to include
        if count == k:

            # Start answer pointer
            if not start:
                start = curr

            # Point last to curr
            if last:
                last.next = curr

            last = curr

            # Reset counter
            count = 0
            
        curr = curr.next
        count += 1

    # Remove nodes between last kth and end
    if last:
        last.next = None

    return start


def printL(n):
    while n:
        print(n.value)
        n = n.next
    print("---")

l1 = ListNode(1,ListNode(2,ListNode(3,ListNode(4,ListNode(5,ListNode(6,ListNode(7)))))))
# new1 = everyKthNode(l1, 3)
# printL(new1)

new1 = everyKthNode(l1, 20)
printL(new1)
