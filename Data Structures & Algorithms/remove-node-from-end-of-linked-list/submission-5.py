# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        dummy = tail = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n+1):
            fast = fast.next
        
        while fast:
            slow = slow.next
            fast = fast.next
        
        # now slow is the n-1th from end, we got to remove it's next
        slow.next = slow.next.next

        return dummy.next