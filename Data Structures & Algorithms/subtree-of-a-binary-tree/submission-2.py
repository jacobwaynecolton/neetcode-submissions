class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        sub_root_valid = False

        if not root and not subRoot:
            return True

        def check_structure(node, subtree_node):
            if not node and not subtree_node:
                return True
            if not node or not subtree_node:
                return False
            if node.val == subtree_node.val:
                left = check_structure(node.left, subtree_node.left)
                right = check_structure(node.right, subtree_node.right)
                if left and right:
                    return True
            return False

        def dfs(node):
            nonlocal sub_root_valid
            if not node:
                return None
            if node.val == subRoot.val:
                if check_structure(node, subRoot):
                    sub_root_valid = True
                    return True
            left = dfs(node.left)
            right = dfs(node.right)
            return False

        dfs(root)
        
        return sub_root_valid