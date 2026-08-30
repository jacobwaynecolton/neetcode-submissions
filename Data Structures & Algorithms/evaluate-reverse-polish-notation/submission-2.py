class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        # Solving using a stack data structure
        # Iterating through the list, pushing each new element onto the stack
        # once an operator is reached, pop the left and right operands off of the stack
        # append the output onto the stack. Repeat until only one output is left


        stack = []

        for token in tokens:
            if token not in '+-*/':
                stack.append(float(token))
            else:
                # pop the right and left operands off of the stack
                right = stack.pop()
                left = stack.pop()

                if token == '+':
                    stack.append(left + right)
                elif token == '-':
                    stack.append(left - right)
                elif token == '*':
                    stack.append(left * right)
                else:
                    # using int here to immediately truncate the division result 
                    stack.append(int(left / right))
        
        return int(stack.pop())