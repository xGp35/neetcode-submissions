"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return head
        copy_map = {}
        head2 = Node(head.val, None, None)
        copy_map[head]= head2

        curr1 = head.next
        curr2 = head2
        while curr1:
            new = Node(curr1.val, None, None)
            curr2.next = new
            copy_map[curr1]= new

            curr1 = curr1.next
            curr2 = curr2.next

        curr1 = head
        curr2 = head2
        while curr1:
            if curr1.random:
                curr2.random = copy_map[curr1.random]
            curr1 = curr1.next
            curr2 = curr2.next
        return head2
