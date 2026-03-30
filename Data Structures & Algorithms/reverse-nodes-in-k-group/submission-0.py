# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseKGroup(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode(0,head)
        groupPrev = dummy
        temp = head

        # This temp node with jump between groups.
        # 1st it points to first group head, 
        # then to the next group first node & so on
        while temp:
            kth = self.getKth(temp, k)
            if not kth:
                if groupPrev: groupPrev.next = temp;
                break
            groupNext = kth.next
            kth.next = None

            self.reverse(temp)

            if temp == head: # This will run only if head is the first node
                head = kth   # In that case we set fisrt kth node to head.
            else:
                groupPrev.next = kth

            groupPrev = temp # just remembering what was temp before moving it.
            temp = groupNext
        return head

             
    def getKth(self,curr, k):
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