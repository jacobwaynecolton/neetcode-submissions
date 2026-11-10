from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        # Implement a BFS approach using a queue

        if not root:
            return []

        # Creating a queue
        queue = deque()
        
        # Adding the first node to the queue
        queue.append(root)

        output = []

        # While there are still nodes in the queue, loop
        while queue:
            # Check the length of the queue (thats the amount of 
            # nodes in the next layer)
            next_lay_count = len(queue)
            print('next count : ', next_lay_count)
            
            # Iterate over the layer
            for i in range(next_lay_count):
                cur_node = queue.popleft()

                # If it's the first node of the layer append its val
                # if it has children, append them
                if i == 0:
                    output.append(cur_node.val)
                if cur_node.right:
                    queue.append(cur_node.right)
                if cur_node.left:
                    queue.append(cur_node.left)

        return output

