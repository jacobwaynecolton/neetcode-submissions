class Solution:
    def isValid(self, s: str) -> bool:
        # Order matters, so keeping count will not suffice
        # stack approach, FIFO
        stack = []
        for character in s:
            if character in ('(', '[', '{'):
                if character == '(':
                    character = ')'
                elif character == '[':
                    character = ']'
                elif character == '{':
                    character = '}'
                stack.append(character)
            elif character in (')', ']', '}'):
                if not stack:
                    return False
                if character != stack.pop():
                    return False
        if stack:
            return False
        return True