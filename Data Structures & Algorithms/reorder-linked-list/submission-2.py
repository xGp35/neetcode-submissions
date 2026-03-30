# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        
        current = slow = fast = head
        l = 1

        #Find middle 

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
            l += 2

        # Now slow is the middle of the list.
        if l <= 2:
            return
        #Now reverse the list after middle

        curr = slow
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        
        # Now prev is now the head of end of linked list
        # Now merge the list from head and prev

        tail = head  
        current1 = head.next
        current2 = prev
        count = 0

        while current1 and current2:
            if count%2 == 0 :
                tail.next = current2
                current2 = current2.next
            else:
                tail.next = current1
                current1 = current1.next

            tail = tail.next
            count += 1

        return




