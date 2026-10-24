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
        old_to_new = {None:None}

        cur = head
        while cur:
            old_to_new[cur]=Node(cur.val)
            cur = cur.next
        
        cur = head

        while cur:
            new = old_to_new[cur]
            new.next = old_to_new[cur.next]
            new.random = old_to_new[cur.random]
            new = new.next
            cur = cur.next

        return old_to_new[head]

            