# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def invertTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        # Writing this as a recursive algorithm

        # Base case :
        if not root:
            return None
        else:
            # Swap the child nodes
            placeholder_node = self.invertTree(root.left)
            root.left = self.invertTree(root.right)
            root.right = placeholder_node

            # return the root
            return root