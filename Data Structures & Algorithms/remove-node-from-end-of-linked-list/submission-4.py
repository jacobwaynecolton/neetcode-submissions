# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Creating a slower pointer and a fast pointer
        # the slow pointer will stay n spaces behind the fast pointer 

        # I need to remember that I can use the head variable directly in the return statement
        # so long as I don't change head itself. Meaning, I don't need to store a temp_head 
        # variable to keep the object's address

        slow_pointer = fast_pointer = head 
        
        # Moving the fast pointer n - 1 places in the linked list, so the slow pointer
        # will be at the element which needs to be removed when the fast pointer reaches the end
        for _ in range (n - 1):
            fast_pointer = fast_pointer.next

        # Keeping track of the node prior to the slow pointer
        prev_slow_pointer = None

        # Iterate until the fast pointer reaches the end 
        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            prev_slow_pointer = slow_pointer
            slow_pointer = slow_pointer.next
        
        if prev_slow_pointer:
            prev_slow_pointer.next = slow_pointer.next
        else:
            return slow_pointer.next
        return head