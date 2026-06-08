# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # 3 steps to reorder
        
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        #now slow is at midpoint

        prev = temp = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        curr1 = head.next
        curr2 = prev
        tail = head
        count = 0

        while curr1 and curr2:
            if count % 2 == 0:
                tail.next = curr2
                curr2 = curr2.next
            else:
                tail.next = curr1
                curr1 = curr1.next
            tail = tail.next
            count += 1
        return
