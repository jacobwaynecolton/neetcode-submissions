class ListNode:
    def __init__(self,next,val):
        self.next = next
        self.val = val

class LinkedList:
    
    def __init__(self):
        self.head = None
        self.tail = None

    
    def get(self, index: int) -> int:
        # Creating a temp node for iterating through the list
        temp = self.head

        if not temp:
            return -1 

        for i in range(index):
            if not temp.next:
                return -1
            temp = temp.next
        
        return temp.val
        

    def insertHead(self, val: int) -> None:
        new_node = ListNode(self.head,val)

        if not self.head:
            self.head = new_node
        else:
            new_node.next = self.head
            self.head = new_node
        if not self.tail:
            self.tail = new_node
        

        


    def insertTail(self, val: int) -> None: 
        new_node = ListNode(None,val)

        if self.tail:
            self.tail.next = new_node
            self.tail = new_node
        elif self.head:
            self.head.next = new_node
            self.tail = new_node
        else:
            self.head = new_node
            self.tail = new_node

    def remove(self, index: int) -> bool:
        if index == 0:
            if not self.head:
                return False
            else:
                self.head = self.head.next
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

        if temp:
            val_arr.append(temp.val)
        else:
            return []

        while temp.next:
            temp = temp.next
            val_arr.append(temp.val)

        return val_arr
        
