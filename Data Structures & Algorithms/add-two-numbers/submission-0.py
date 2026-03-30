# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        carry = 0
        dummy = ListNode(0, l1)
        tail = dummy
        while l1 and l2 and tail:
            temp = l1.val + l2.val + carry
            l1.val = temp % 10
            carry = temp // 10

            l1 = l1.next
            l2 = l2.next
            tail = tail.next

        tail.next = l1 or l2
        if not tail.next and carry:
            new = ListNode(carry, None)
            tail.next = new

        else:
            tail2 = tail
            tail = tail.next
            while tail:
                temp = tail.val + carry 
                tail.val = temp % 10
                carry = temp // 10
                tail = tail.next
                tail2 = tail2.next
            if not tail2.next and carry:
                new = ListNode(carry, None)
                tail2.next = new

        
        return dummy.next
        
