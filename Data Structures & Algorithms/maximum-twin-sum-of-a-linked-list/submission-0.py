# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow = head
        fast = head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        temp = slow.next
        slow.next = None

        new_head = self.reverse(head)

        maxTwin = float('-inf')
        curr1, curr2 = new_head, temp
        while curr1 and curr2:
            maxTwin = max(maxTwin, curr1.val + curr2.val)
            curr1 = curr1.next
            curr2 = curr2.next
        if curr1: maxTwin = max(maxTwin, curr1.val)
        if curr2: maxTwin = max(maxTwin, curr2.val)
        return maxTwin

    
    def reverse(self, head):
        curr, prev = head, None

        while curr:
            tmp = curr.next
            curr.next = prev
            prev = curr
            curr = tmp

        return prev

        
