# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        dummy = ListNode(0)
        tail = dummy
        carry = 0
        curr1, curr2 = l1, l2
        while curr1 or curr2:
            a = curr1.val if curr1 else 0
            b = curr2.val if curr2 else 0
            sum_val = (carry + a + b) % 10
            carry = (carry + a + b) // 10
            new_node = ListNode(sum_val)
            tail.next = new_node
            tail = tail.next
            curr1 = curr1.next if curr1 else None
            curr2 = curr2.next if curr2 else None
        
        if carry: 
            tail.next = ListNode(1)
        
        return dummy.next
    




