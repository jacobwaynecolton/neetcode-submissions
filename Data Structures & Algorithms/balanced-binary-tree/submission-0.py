# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:

        # Nested recursive function solution
        # Keeping track of whether there is a height violation
        self.is_height_balanced = True


        # Creating a nested dfs function to gather subtree heights
        def dfs(node):

            # Base case
            if not node:
                return 0
            
            left = dfs(node.left)
            right = dfs(node.right)

            # Checking the height difference
            if abs(left-right) > 1:
                self.is_height_balanced = False
            
            return 1 + max(left,right)
        
        dfs(root)
        return self.is_height_balanced

            
        

        