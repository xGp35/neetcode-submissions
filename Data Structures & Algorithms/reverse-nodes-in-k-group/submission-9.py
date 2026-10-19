# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = groupPrev = ListNode(0, head)
        curr = head
    
        while curr:
            kth = self.getKth(curr, k)
            if not kth:
                break

            groupNext = kth.next
            kth.next = None
            self.reverse(curr)

            groupPrev.next = kth # This literally fixes the thing you're worrying about. before moving groupPrev, you assign the older groupPrev to first element of the reversed group.
            groupPrev = curr
            curr = groupNext

        groupPrev.next = curr
        return dummy.next
        
    def getKth(self, head, k):
        curr = head
        while curr and k > 1:
            curr = curr.next
            k -= 1
        return curr
    
    def reverse(self, head):
        prev, curr = None, head

        while curr:
            temp = curr.next
            curr.next = prev
            prev = curr
            curr = temp

        
