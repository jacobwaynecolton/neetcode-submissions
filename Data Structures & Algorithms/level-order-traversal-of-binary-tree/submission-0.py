# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        # Creating a dictionary of lists. One list for each level
        lvls = {}

        # Creating a dfs which tracks height/lvl
        # This dfs will need to travel left to right
        def dfs(node, lvl):
            if not node:
                return
            if lvl in lvls:
                # If this level is in levels insert the current
                # node into that list
                lvls[lvl].append(node.val)
            else:
                lvls[lvl] = [node.val]

            # Traversing the tree left to right
            dfs(node.left, lvl + 1)
            dfs(node.right, lvl + 1)

        dfs(root, 0)
        return [lvls[key] for key in lvls.keys()]