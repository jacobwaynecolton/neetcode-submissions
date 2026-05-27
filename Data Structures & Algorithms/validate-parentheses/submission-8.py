class Solution:
    def isValid(self, s: str) -> bool:
        # Starting over with LIFO, but this time using dictionary,
        # because the dictionary only needs to have 3 elements
        valid_pairs = {'(' :')', '[':']', '{':'}'}
        stack = []

        for character in s:
            if character in valid_pairs:
                stack.append(character)
            elif character in (']',')','}'):
                if not stack:
                    return False
                elif character != valid_pairs[stack.pop()]:
                    return False
        return not stack
        