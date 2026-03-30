# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Get the midpoint using slow and fast pointers
        # Reverse the second part
        # Zip the first and reversed second past together
        
        slow = fast = head
        
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        
        # Now slow is at the midpoint
        #Reverse the list starting from midpoint

        prev = temp = None
        curr = slow

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Now prev holds the last element pointer
        # Now I need to zip lists starting from head and prev.

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



