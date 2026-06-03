class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        # Nested function to check the subtree structure matches
        def check_structure(node, subtree_node):
            if not node and not subtree_node:
                return True
            if not node or not subtree_node:
                return False
            if node.val == subtree_node.val:
                # Traversing down the subtree candidate
                left = check_structure(node.left, subtree_node.left)
                right = check_structure(node.right, subtree_node.right)
                # return true if both subtrees match
                return left and right
            return False
        # DFS function to traverse the tree, identifying potential
        # subtrees, via checking the root value
        def dfs(node):
            if not node:
                return False
            # check if it's a potential subtree match
            if node.val == subRoot.val:
                # use the other nested function to verify if it's
                # a full match
                if check_structure(node, subRoot):
                    return True
            # Putting the two dfs recursive calls in the return statement
            # separated by an or operator so that short-circuiting may
            # prevent unnecessary searching
            return dfs(node.left) or dfs(node.right)

        return dfs(root)