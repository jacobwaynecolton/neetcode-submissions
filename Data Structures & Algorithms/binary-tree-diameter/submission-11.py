# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        
        # Creating a nested recursive function, as we must 
        # maintain track of what the current longest path is 

        self.longest_path = 0      

        # Modifying the dfs nested function to return the larger
        # of a root's two branches, as well as update the current
        # longest path in the tree
        def dfs(root):

            if not root:
                return 0
            left = dfs(root.left)
            right = dfs(root.right)
            current_longest_path = left + right

            if current_longest_path > self.longest_path:
                self.longest_path = current_longest_path
            return 1 + max(left,right)
        
        dfs(root)
        return self.longest_path
        