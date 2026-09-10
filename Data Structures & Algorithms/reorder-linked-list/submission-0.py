# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reorderList(self, head: Optional[ListNode]) -> None:
        # Creating a stack storing the linked list in a reverse order
        stack = []

        if not head:
            return 

        head_save = head
        cur_node = head

        while cur_node.next:
            stack.append(cur_node)
            cur_node = cur_node.next
        
        stack.append(cur_node)

        left_node = head_save
        right_node = stack.pop()

        while (left_node is not right_node) and right_node is not left_node.next: 
            next_node = left_node.next
            left_node.next = right_node
            right_node.next = next_node
            left_node = next_node
            if not stack:
                right_node.next = None
                return
            right_node = stack.pop()
        right_node.next = None
        
       