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
        copy_dict = {None: None}

        curr = head

        while curr:
            new_node = Node(curr.val)
            copy_dict[curr] = new_node
            curr = curr.next
        
        curr = head
        while curr:
            copy_dict[curr].next = copy_dict[curr.next]
            copy_dict[curr].random = copy_dict[curr.random]
            curr = curr.next

        return copy_dict[head]
