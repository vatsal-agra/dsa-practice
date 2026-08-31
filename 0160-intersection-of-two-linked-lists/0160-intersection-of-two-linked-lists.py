# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> Optional[ListNode]:
        nodea = headA
        nodeb = headB
        while nodea != nodeb:
            nodea = headB if nodea == None else nodea.next
            nodeb = headA if nodeb == None else nodeb.next
        return nodea