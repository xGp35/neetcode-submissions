# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:

        def reverse(node):
            curr = node
            prev, temp = None, None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        lr1 = l1
        lr2 = l2

        dummy = ListNode(0)
        tail = dummy

        carry = 0

        l1 = reverse(lr1)
        l2 = reverse(lr2)

        while l1 and l2:
            total = l1.val + l2.val + carry

            value = total % 10
            carry = total //10

            newNode = ListNode(value)
            tail.next = newNode
            tail = tail.next

            l1 = l1.next
            l2 = l2.next

        while l1:
            total = l1.val + carry
            value = total % 10
            carry = total //10
            newNode = ListNode(value)
            tail.next = newNode
            tail = tail.next
            l1 = l1.next
        
        while l2:
            total = l2.val + carry
            value = total % 10
            carry = total //10
            newNode = ListNode(value)
            tail.next = newNode
            tail = tail.next
            l2 = l2.next
        
        if carry:
            newNode = ListNode(carry)
            tail.next = newNode
            tail = tail.next
        
        temp = dummy.next
        dummy.next = None
        res = reverse(temp)


        return res

        