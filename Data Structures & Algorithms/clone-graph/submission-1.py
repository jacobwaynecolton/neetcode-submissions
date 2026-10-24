"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        # Creating a dict to store all of the seen values
        new_graph = {}
       
        if not node:
            return None

        # Creating a recursive function which will go to neighboring nodes, adding the val to seen, instantiating, & interconnecting
        def dfs(node):
            if node.val not in new_graph:
                new_neighbors = []
                # Intantiating for the new graph
                copy_node = Node(node.val,[])
                # putting the copy in the new graph
                new_graph[node.val] = copy_node
                # Iterating through its neighbors
                for neighbor in node.neighbors: 
                    if neighbor.val in new_graph:
                        new_neighbors.append(new_graph[neighbor.val])
                    else:
                        new_neighbors.append(dfs(neighbor))
                copy_node.neighbors = new_neighbors

                return copy_node

        return dfs(node)
               

            


        