class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # verifying if the two strings are of equal length
        # doing this initially do allow for returns prior to declarations
       if len(s) != len(t) : 
            return False


       seen_chars = [0]*26
       # They are the same length iterable, meaning we can use a zip
       # to iterate through both simeoultaneously
       for a,b in zip(s,t):
            seen_chars[ord(a) - ord('a')] += 1
            seen_chars[ord(b) - ord('a')] -= 1
        
       return not any(seen_chars)
      

