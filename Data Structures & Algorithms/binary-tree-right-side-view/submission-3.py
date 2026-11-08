# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # making a set to represent which levels have a seen entry
        seen_lvls = set()
        output = []

        # Using dfs but keeping track of the level and adding to dict
        # if there's no node for that level
        def dfs(node,lvl):
            if not node:
                return
            if lvl not in seen_lvls:
                seen_lvls.add(lvl)
                output.append(node.val)
            dfs(node.right,lvl+1)
            dfs(node.left,lvl+1)
            

        dfs(root,0)
        return output



