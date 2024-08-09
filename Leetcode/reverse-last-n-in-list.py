# def solution(balances, requests):
    
#     #transfer i j sum    
#     #deposit i sum    
#     #withdraw i sum
        
#     #invalid account
#     #withdraw/transfer in excess
    
#     # return balances after all successful operations OR [-<request_id>] if invalid request received

#     requests = [[request.split(" ")[0]] + [int(x) for x in request.split(" ")[1:]] for request in requests]
    
#     for i, request in enumerate(requests):
        
#         def validateAccNum(accNum):
#             return len(balances) > accNum
            
#         def validateAccNumBalance(accNum, amt):
#             return balances[accNum] >= amt
        
#         if request[0] == "withdraw":
#             accNum = request[1] - 1
#             rSum = request[2]
            
#             # check valid account
#             # check valid amount
#             if not validateAccNum(accNum) or not validateAccNumBalance(accNum, rSum):
#                 return [-i-1]
                
#             # process request
#             balances[accNum] -= rSum
            
#         if request[0] == "transfer":
#             senderAccNum = request[1] - 1
#             receiverAccNum = request[2] - 1
#             rSum = request[3]
            
#             # check valid accounts
#             # check valid amount
#             if not validateAccNum(senderAccNum) or not validateAccNum(receiverAccNum) or not validateAccNumBalance(senderAccNum, rSum):
#                 return [-i-1]
                
#             # process request
#             balances[senderAccNum] -= rSum
#             balances[receiverAccNum] += rSum
            
#         if request[0] == "deposit":
            
#             accNum = request[1] - 1
#             rSum = request[2]
            
#             # check valid account
#             if not validateAccNum(accNum):
#                 return [-i-1]
                
#             # process request
#             balances[accNum] += rSum

#     return balances
    
    

# # print(solution(balances = [10, 100, 20, 50, 30], requests =
# # ["withdraw 2 10", 
# #  "transfer 5 1 20", 
# #  "deposit 5 20", 
# #  "transfer 3 4 15"]))

# Singly-linked lists are already defined with this interface:
class ListNode(object):
  def __init__(self, x, next = None):
    self.value = x
    self.next = next

def solution(head, n):
    
    if not head:
        return None

    lenL = 0
    c = head
    while c:
        lenL += 1
        c = c.next

    slow = None
    fast = None
    
    for _ in range(min(lenL, n)):
        if not fast:
            fast = head
        else:
            fast = fast.next
        
    # fast is n ahead of slow
    
    while fast.next:
        fast = fast.next

        if not slow:
            slow = head
        else:
            slow = slow.next
        
    # fast is at null
    # slow is at point in list that newly flipped portion should point to
    
    tail = slow

    if slow:
        slow = slow.next
    else:
        slow = head

    last = None
    
    while slow:
        nextN = slow.next
        slow.next = last
        last = slow
        slow = nextN
    
    if tail:
        tail.next = last

    if lenL <= n:
        return fast
    else:
        return head

def printL(flipped):
    while flipped:
        print(flipped.value)
        flipped = flipped.next
    print("----")

list1 = ListNode(1, ListNode(2, ListNode(3, ListNode(5, ListNode(4)))))
printL(list1)
flipped = solution(list1, 2)
printL(flipped)
print("++++++++")

list2 = ListNode(5, ListNode(4, ListNode(3, ListNode(2, ListNode(1)))))
printL(list2)
flipped = solution(list2, 5)
printL(flipped)
print("++++++++")