# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        
        curr = temp = head
        leng = 0
        while curr:
            leng += 1 
            curr = curr.next
        
        req = leng - n

        if req == 0:
            head = head.next
            return head

        curr = temp
        count = 0
        while curr:
            count += 1
            if count == req:
                curr.next = curr.next.next
                return head
            curr = curr.next
        
        return head