"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        if node is None:
            return None

        # original node -> cloned node
        old_to_new = {}

        def dfs(curr):
            # Already cloned
            if curr in old_to_new:
                return old_to_new[curr]

            # Create clone
            copy = Node(curr.val)
            old_to_new[curr] = copy

            # Clone all neighbors
            for neighbor in curr.neighbors:
                copy.neighbors.append(dfs(neighbor))

            return copy

        return dfs(node)
        