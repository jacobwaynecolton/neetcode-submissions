# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def reverseList(self, head: Optional[ListNode]) -> Optional[ListNode]:

        # Keeping track of the previous ListNode
        prev = None

        # Keeping track of the current ListNode
        if head:
            cur = head
        else:
            return None 
        # Keeping track of the following ListNode
        next = None

        # While there is a cur list node, iterate through the linked list
        while cur.next:
            next = cur.next
            cur.next = prev
            prev = cur
            cur = next
            
        # If there is no previous list node (the list contains a sole element)
        if not prev:
            return cur
        else:
            cur.next = prev

        return cur