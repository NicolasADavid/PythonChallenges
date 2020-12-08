# Reverse Operations
# You are given a singly-linked list that contains N integers. A subpart of the list is a contiguous set of even elements, bordered either by the end of the list or an odd element. For example, if the list is [1, 2, 8, 9, 12, 16], the subparts of the list are [2, 8] and [12, 16].
# Then, for each subpart, the order of the elements is reversed. In the example, this would result in the new list, [1, 8, 2, 9, 16, 12].
# The goal of this question is: given a resulting list, determine the original order of the elements.
# Implementation detail:
# You must use the following definition for elements in the linked list:
# class Node {
#     int data;
#     Node next;
# }
# Signature
# Node reverse(Node head)
# Constraints
# 1 <= N <= 1000, where N is the size of the list
# 1 <= Li <= 10^9, where Li is the ith element of the list
# Example
# Input:
# N = 6
# list = [1, 2, 8, 9, 12, 16]
# Output:
# [1, 8, 2, 9, 16, 12]


import math
# Add any extra import statements you may need here


class Node:
  def __init__(self, x):
    self.data = x
    self.next = None

# Add any helper functions you may need here


def reverse(head):
  if not head: return None
  
  subListPrev = None
  subListNext = None
  subListHead = None
  subListTail = None
  
  curr = head
  
  while curr:
      
      # As odd-valued nodes are found, move subListPrev
      if curr.data % 2 == 1:
          subListPrev = curr
          curr = curr.next
          
      # found start of sublist of even-valued nodes
      else:
          
          prev = None
          subListHead = curr
          subListTail = curr
          
          while curr and curr.data % 2 == 0:
              next = curr.next
              curr.next = prev
              prev = curr
              subListTail = curr
              curr = next
      
          # Curr is now an odd-valued node or None
          subListNext = curr
          
          # point subListPrev if defined to head of the list
          # point subListTail (original) to subListNext
          subListHead.next = subListNext
          
          if subListPrev:    
              subListPrev.next = subListTail
          else:
              head = subListTail
  
  return head











# These are the tests we use to determine if the solution is correct.
# You can add your own at the bottom, but they are otherwise not editable!

def printLinkedList(head):
  print('[', end='')
  while head != None:
    print(head.data, end='')
    head = head.next
    if head != None:
      print(' ', end='')
  print(']', end='')

test_case_number = 1

def check(expectedHead, outputHead):
  global test_case_number
  tempExpectedHead = expectedHead
  tempOutputHead = outputHead
  result = True
  while expectedHead != None and outputHead != None:
    result &= (expectedHead.data == outputHead.data)
    expectedHead = expectedHead.next
    outputHead = outputHead.next

  if not(outputHead == None and expectedHead == None):
    result = False

  rightTick = '\u2713'
  wrongTick = '\u2717'
  if result:
    print(rightTick, ' Test #', test_case_number, sep='')
  else:
    print(wrongTick, ' Test #', test_case_number, ': Expected ', sep='', end='')
    printLinkedList(tempExpectedHead)
    print(' Your output: ', end='')
    printLinkedList(tempOutputHead)
    print()
  test_case_number += 1

def createLinkedList(arr):
  head = None
  tempHead = head
  for v in arr:
    if head == None:
      head = Node(v)
      tempHead = head
    else:
      head.next = Node(v)
      head = head.next
  return tempHead

if __name__ == "__main__":
  head_1 = createLinkedList([1, 2, 8, 9, 12, 16])
  expected_1 = createLinkedList([1, 8, 2, 9, 16, 12])
  output_1 = reverse(head_1)
  check(expected_1, output_1)

  head_2 = createLinkedList([2, 18, 24, 3, 5, 7, 9, 6, 12])
  expected_2 = createLinkedList([24, 18, 2, 3, 5, 7, 9, 12, 6])
  output_2 = reverse(head_2)
  check(expected_2, output_2)

  # Add your own test cases here
  