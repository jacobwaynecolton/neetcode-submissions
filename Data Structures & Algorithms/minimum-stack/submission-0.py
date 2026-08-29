class MinStack:

    def __init__(self):
        # Creating array to keep track of the order the elements were pushed
        self.order_arr = []
        # Creating an array which has the elements sorted
        self.min_arr = []

    def push(self, val: int) -> None:
        # appending the new element to the ordered array
        self.order_arr.append(val)
        # appending the new element to the minimum array only if it is less
        # than the current minimum. Otherwise, append a duplicate of the current
        # minimum to keep the min array matching the ordered array in length.
        # This is so that the pop method remains synchronized
        if len(self.min_arr) > 0 and self.min_arr[-1] < val:
            self.min_arr.append(self.min_arr[-1])
        else:
            self.min_arr.append(val)

    def pop(self) -> None:
        # pop from both the min and ordered arrays
        self.min_arr.pop()
        self.order_arr.pop()

    def top(self) -> int:
        # return the most recently added element
        return self.order_arr[-1]

    def getMin(self) -> int:
        # return the minimum element from the min array 
        return self.min_arr[-1]