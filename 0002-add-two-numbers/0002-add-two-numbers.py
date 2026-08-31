# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        op1 = l1
        op2 = l2
        dummy = ListNode()
        tail = dummy
        carry = 0
        while op1 or op2 or carry:
            v1 = op1.val if op1 else 0
            v2 = op2.val if op2 else 0
            val = v1 + v2 + carry

            carry = val // 10
            tail.next = ListNode(val%10)                

            
            tail = tail.next
            op1 = op1.next if op1 else None
            op2 = op2.next if op2 else None
        return dummy.next