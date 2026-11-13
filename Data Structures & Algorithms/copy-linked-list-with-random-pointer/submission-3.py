"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        # Creating a dict where the keys are nodes from the original 
        # linked list and the values are the corresponding nodes 
        # from the new linked list 
        prev_to_new = dict()
        first_node = None
        cur_node = head
        prev_node = None

        while cur_node:
            # If the current node leads to a random node, get its copy
            # or make its copy
            rand_copy = None
            if cur_node.random:
                # If the corresponding node already exists in our dict
                # use that for the rand_copy
                if cur_node.random in prev_to_new:
                    rand_copy = prev_to_new[cur_node.random]
                else:
                    # Creating the random copy, but leaving
                    # its pointers blank for now
                    rand_copy = Node(cur_node.random.val,None,None)
                    # Store it 
                    prev_to_new[cur_node.random] = rand_copy


            # Create the copy of the current node if it's not already
            # in the dictionary  
            # leave the next pointer blank for now
            if cur_node in prev_to_new:
                cur_copy = prev_to_new[cur_node]
                # update the random pointer
                cur_copy.random = rand_copy
            else:
                cur_copy = Node(cur_node.val,None,rand_copy)
                # put it in the dict
                prev_to_new[cur_node] = cur_copy


            # If there was a previous node, update its next value
            # to our current node
            if prev_node:
                prev_node.next = cur_copy
            
            # update prev_node
            prev_node = cur_copy
            # update cur_node
            cur_node = cur_node.next



        # If there is a head in this new linked list to return, return it
        if head in prev_to_new:
            return prev_to_new[head]
        else:
            return None
       