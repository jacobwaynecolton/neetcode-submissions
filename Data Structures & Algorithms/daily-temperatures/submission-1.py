class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        # If the there are no temperatures, return an empty list
        if not temperatures:
            return []

        # Set the starting temp to infinity to guarantee the next will be less
        stack = []
        prev_temp = math.inf

        # Creating a placeholder array to assign values to
        output = [0] * len(temperatures)
        
        # If the next temp is less than the current, push it to the stack
        for i,temp in enumerate(temperatures):
            # If the current temp is <= to the previous temp,
            # append it and update the previous temp
            if temp <= prev_temp:
                prev_temp = temp
                stack.append((temp,i))
            # Otherwise, if the current temp is > the previous temp
            # iterate through the stack popping off all elements
            # which are less than the current temp, and updating
            # their placeholder value in the output to be the difference
            # between the current index and the temp's index in the list
            else:
                while stack and temp > stack[-1][0]:
                    output[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                
                stack.append((temp,i))
            
        return output