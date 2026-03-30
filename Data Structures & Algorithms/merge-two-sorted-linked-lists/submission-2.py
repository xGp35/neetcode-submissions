# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        if not list1:
            return list2
        if not list2:
            return list1
        
        if list2.val < list1.val:
            temp = list1
            list1 = list2
            list2 = temp

        tail = list1
        current1 = list1.next
        current2 = list2
    
        while current1 and current2:
            if current1.val <= current2.val:
                 tail.next = current1
                 current1 = current1.next
            else:
                tail.next = current2
                current2 = current2.next
            
            tail = tail.next

        if current1:
            tail.next = current1
        if current2:
            tail.next = current2

        return list1