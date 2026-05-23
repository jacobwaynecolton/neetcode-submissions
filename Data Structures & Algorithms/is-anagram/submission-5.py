class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
       # Duplicate character counts need to also be considered
       # This means that a dictionary must be used instead of a set
       seen_chars = {}

       # verifying if the two strings are of equal length
       if len(s) != len(t) : 
            return False

       # iterating through the first string
       for letter in s:
            # using the dictionary's get function with a default value
            # of 0 to get the current numeric value of the associated
            # character
            seen_chars[letter] = seen_chars.get(letter,0) + 1
        
        # iterating through the letters in the second string
       for letter in t:
            if letter not in seen_chars:
                return False
            
            seen_chars[letter] -=1
            if seen_chars[letter] < 0:
                return False
        
       return True
      

