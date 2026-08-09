# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:


        head_1 = list1
        head_2 = list2


        return_list_head=None

        return_list_head_fixed = None


        while head_1 is not None or head_2 is not None:
            if head_1 is None:
                head_to_add = head_2
                head_2 = head_2.next
            elif head_2 is None:
                head_to_add = head_1                    
                head_1 = head_1.next
            else:
                if head_1.val < head_2.val:
                    head_to_add = head_1                    
                    head_1 = head_1.next
                else:
                    head_to_add = head_2
                    head_2 = head_2.next
                
            if return_list_head is None:
                return_list_head = head_to_add
                return_list_head_fixed = return_list_head
            else:
                return_list_head.next = head_to_add
                return_list_head = return_list_head.next
        return return_list_head_fixed
                


        