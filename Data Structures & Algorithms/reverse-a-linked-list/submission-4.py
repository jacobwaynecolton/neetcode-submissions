# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        if not head :
            return None
        
        if head.next is None:
            return head

        current_node = head.next
        head.next = None
        prev_node = head
        next_node = None
        # Updating the head node to be the tail node
        while current_node is not None and current_node.next is not None:
            next_node = current_node.next
            current_node.next = prev_node
            prev_node = current_node
            current_node = next_node
        current_node.next = prev_node
        
        return current_node

            