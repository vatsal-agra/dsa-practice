# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
import math
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head
        while curr.next:
         #   a = curr.val
         #   b = curr.next.val
            after = curr.next
            val = ListNode(math.gcd(curr.val,curr.next.val))
            curr.next = val
            val.next = after
            curr = after
        return head