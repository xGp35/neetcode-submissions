# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        minHeap = []
        counter = count()
        for head in lists:
            heapq.heappush(minHeap, (head.val, next(counter), head))
        
        dummy = ListNode()
        tail = dummy

        while minHeap:
            val, _ , node = heapq.heappop(minHeap)
            tail.next = node
            if node.next:
                heapq.heappush(minHeap, (node.next.val, next(counter), node.next))
            tail = tail.next
        return dummy.next