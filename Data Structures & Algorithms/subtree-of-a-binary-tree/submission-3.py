class Solution:
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        def check_structure(node, subtree_node):
            if not node and not subtree_node:
                return True
            if not node or not subtree_node:
                return False
            if node.val == subtree_node.val:
                left = check_structure(node.left, subtree_node.left)
                right = check_structure(node.right, subtree_node.right)
                return left and right
            return False

        def dfs(node):
            if not node:
                return False
            if node.val == subRoot.val:
                if check_structure(node, subRoot):
                    return True
            return dfs(node.left) or dfs(node.right)

        return dfs(root)