class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        if not temperatures:
            return []

        stack = []
        cur_temp = math.inf

        output = [0] * len(temperatures)
        
        # If the next temp is less than the current, push it to the stack
        for i,temp in enumerate(temperatures):
            if temp <= cur_temp:
                cur_temp = temp
                stack.append((temp,i))
            else:
                while stack and temp > stack[-1][0]:
                    output[stack[-1][1]] = i - stack[-1][1]
                    stack.pop()
                
                stack.append((temp,i))
            
        return output