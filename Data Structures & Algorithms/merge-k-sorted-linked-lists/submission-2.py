# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:    
    def mergeKLists(self, lists: List[Optional[ListNode]]) -> Optional[ListNode]:
        if not lists or len(lists) == 0: return None

        minHeap = []
        heapq.heapify(minHeap)
        for i, head in enumerate(lists):
            heapq.heappush(minHeap, (head.val, i, head))
        
        dummy = tail = ListNode()

        while minHeap:
            val, i, node = heapq.heappop(minHeap)
            tail.next = node
            tail = node
            if node.next:
                heapq.heappush(minHeap, (node.next.val, i, node.next))
        
        return dummy.next