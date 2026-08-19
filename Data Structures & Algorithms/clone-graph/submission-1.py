"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if not node:
            return None
        oldToNew = {}
        def clone(node):
            if node in oldToNew:
                return oldToNew[node]
            
            new_node = Node(node.val)
            oldToNew[node] = new_node

            for i in node.neighbors:
                new_node.neighbors.append(clone(i))
            
            return new_node
        return clone(node)