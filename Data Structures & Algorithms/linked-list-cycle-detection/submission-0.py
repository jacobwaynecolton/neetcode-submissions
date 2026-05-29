# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def hasCycle(self, head: Optional[ListNode]) -> bool:
        cur_node = head
        seen_nodes = set()

        while cur_node:
            seen_nodes.add(cur_node)

            if cur_node.next:
                if cur_node.next in seen_nodes:
                    return True
            
            cur_node = cur_node.next
        
        return False
            
