# Definition for singly-linked list.
# class ListNode:
#test     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        new_list_head =None
        cur_node = None
        if not list1 and not list2:
            return None
        elif not list2:
            return list1
        elif not list1:
            return list2
        if list1.val <= list2.val:
            new_list_head = list1
            cur_node = list1
            list1 = list1.next
        else:
            new_list_head = list2
            cur_node = list2
            list2 = list2.next

        while list1 or list2:
            if not list1:
                cur_node.next = list2
                break
            elif not list2:
                cur_node.next = list1
                break
            if list1.val <= list2.val:
                cur_node.next = list1
                cur_node = list1
                list1 = list1.next
            else:
                cur_node.next = list2
                cur_node = list2
                list2 = list2.next
        return new_list_head

