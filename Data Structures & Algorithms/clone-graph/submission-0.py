"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        old_to_new = {}
        def dfs(cur):
            if cur in old_to_new:
                return old_to_new[cur]
            copy = Node(cur.val)
            old_to_new[cur] = copy
            for neighbour in cur.neighbors:
                copy.neighbors.append(dfs(neighbour))
            return copy
        return dfs(node) if node else None

