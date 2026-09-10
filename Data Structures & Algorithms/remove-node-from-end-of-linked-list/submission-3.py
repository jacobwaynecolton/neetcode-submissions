# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        # Creating a slower pointer and a fast pointer
        # the slow pointer will stay n spaces behind the fast pointer 

        slow_pointer = fast_pointer = head 
        head_save = head

        for i in range (n - 1):
            fast_pointer = fast_pointer.next

        prev_slow_pointer = None

        while fast_pointer.next:
            fast_pointer = fast_pointer.next
            prev_slow_pointer = slow_pointer
            slow_pointer = slow_pointer.next
        
        if prev_slow_pointer:
            prev_slow_pointer.next = slow_pointer.next
        else:
            return slow_pointer.next
        return head