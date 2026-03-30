# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        slow = fast = head

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # Now midpoint is slow

        current = slow.next
        slow.next = None
        prev = None
        temp = None
        while current:
            temp = current.next
            current.next = prev
            prev = current
            current = temp
        
        #Prev is now the head of second list
        dummy = ListNode(0)
        dummy.next = head
        tail = dummy

        count = 0
        list1 = head
        list2 = prev

        while list1 and list2:
            if count % 2 == 0:
                tail.next = list1
                list1 = list1.next
            else:
                tail.next = list2
                list2 = list2.next
            count += 1
            tail = tail.next

        tail.next = list1 or list2
        return


