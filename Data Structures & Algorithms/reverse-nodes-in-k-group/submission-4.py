# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        tail = head
        groupPrev = ListNode(0, head)

        while tail:
            kth = self.getKth(tail, k)
            if not kth:
                break
            groupNext = kth.next
            kth.next = None
            self.reverse(tail)

            if tail == head:
                head= kth
            else:
                groupPrev.next = kth
            
            groupPrev = tail
            tail.next = groupNext
            tail = tail.next
        return head

    def getKth(self, head, k):
        curr = head
        while curr and k > 1:
            curr = curr.next
            k -= 1
        return curr

    def reverse(self, head):
        curr = head
        prev = None

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp
        