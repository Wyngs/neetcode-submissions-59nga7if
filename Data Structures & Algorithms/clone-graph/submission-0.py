"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:

        queue= []
        if not node:
            return None
        else:
            queue.append(node)
        table = {}
        table[node] = Node(node.val)
        while len(queue) != 0:
            curr = queue.pop()
            for i in curr.neighbors:
                if i not in table:
                    table[i] = Node(i.val)
                    queue.append(i)
                table[curr].neighbors.append(table[i])

        return table[node]
        

            

        