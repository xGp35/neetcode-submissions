# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast.next and fast.next.next:
            slow = slow.next
            fast = fast.next.next

        

        def reverse(head):
            curr = head
            prev = None

            while curr:
                temp = curr.next
                curr.next = prev
                prev = curr
                curr = temp
            return prev

        mid = slow.next
        slow.next = None
        end = reverse(mid)
        
        dummy = tail = ListNode(0, head)
        curr1, curr2 = head, end
        count = 0
        while curr1 and curr2:
            if count%2 == 0:
                tail.next = curr1
                curr1 = curr1.next
            else:
                tail.next = curr2
                curr2 = curr2.next
            tail = tail.next
            count += 1
        
        tail.next = curr1 or curr2


        

