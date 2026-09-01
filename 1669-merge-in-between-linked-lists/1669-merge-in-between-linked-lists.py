# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeInBetween(self, list1: ListNode, a: int, b: int, list2: ListNode) -> ListNode:
        before = list1
        for _ in range(a-1):
            before = before.next
        after = before
        for _ in range(b-a+2):
            after = after.next
        tail2 = list2
        while tail2.next:
            tail2 = tail2.next
        before.next = list2
        tail2.next = after
        return list1