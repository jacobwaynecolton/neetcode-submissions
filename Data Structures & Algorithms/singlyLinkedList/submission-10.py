# Creating a ListNode class for the LinkedList class to use 
class ListNode:
    def __init__(self,next,val):
        self.next = next
        self.val = val

class LinkedList:
    
    def __init__(self):
        # Keeping track of the head and tail nodes in the list 
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        # Creating a temp node for iterating through the list
        temp = self.head

        # If there is no head node, return -1
        if not temp:
            return -1 

        for i in range(index):
            if not temp.next:
                return -1
            temp = temp.next
        
        return temp.val
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(self.head,val)

        # If there is no head node, set the list's head to our new node
        if not self.head:
            self.head = new_node
        else:
        # Otherwise, point the new node to the old head then update the list's head
            new_node.next = self.head
            self.head = new_node
        if not self.tail:
        # If there is no tail, also update the tail
            self.tail = new_node
        


    def insertTail(self, val: int) -> None: 
        new_node = ListNode(None,val)

        # If there already is a tail, point it to the new node then update the list's tail
        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        # if there is no tail, but a head, point the head at the tail, and update the list's tail
        elif self.head:
            self.head.next = new_node
            self.tail = new_node
        # if there is no tail, and no head, update them both
        else:
            self.head = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        # If we are removing the first node
        if index == 0:
            if not self.head:
                return False
            else:
                self.head = self.head.next
        # Otherwise iterate through the linked list
        else:
            prev = None
            temp = self.head
            for i in range(index):
                if not temp.next:
                    return False
                else:
                    prev = temp
                    temp = temp.next

            if not temp.next:
                prev.next = None
                self.tail = prev
            else:
                prev.next = temp.next
        
        return True 

        

    def getValues(self) -> List[int]:
        val_arr = []

        temp = self.head
        # If there is a head element append it
        if temp:
            val_arr.append(temp.val)
        else:
            return []
        # While there are more elements which follow it, append them
        while temp.next:
            temp = temp.next
            val_arr.append(temp.val)

        return val_arr
        
