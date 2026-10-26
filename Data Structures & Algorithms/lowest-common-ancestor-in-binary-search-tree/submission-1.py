# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:

        total_node = []
        def dfs(node):
            if not node:
                return 0
            if node.val == q.val:
                return 1
            elif node.val == p.val:
                return 5
            else:
                total = dfs(node.left) + dfs(node.right)
                if total == 6:
                    total_node.append(node)
                    return 0
                else:
                    return total

        
        total = dfs(root)

        if total == 1:
            return q
        elif total == 5:
            return p
        else:
            return total_node[0]
 
            




        