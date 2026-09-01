class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        # if the length of s1 > s2 return false, impossible to contain a permutation
        if len(s1) > len(s2):
            return False

        # Create arrays of 0's of the potential characters (a-z)
        first_count, second_count = [0] * 26, [0] * 26

        # Iterate through the first and second strings, for the amount of characters
        # in the first string, so we can tally up the matches in character & counts
        for i in range(len(s1)):
            # Increasing value of the character's respective index in the array
            # using its ordinal value
            first_count[ord(s1[i]) - ord('a')] += 1
            second_count[ord(s2[i]) - ord('a')] += 1

        # Tallying up the matches
        matches = sum([1 for i in range(26) if first_count[i] == second_count[i]])

        # moving the fixed-size window through the second string
        # starting after what has already been covered (the first string)
        for j in range(len(s1),len(s2)):
            # is the match count correct for each letter in the alphabet?
            if matches == 26:
                # if so, return true
                return True
            
            i = ord(s2[j]) - ord('a')
            # increment the second count's character 
            second_count[i] += 1

            # if that incrementation caused a mismatch, deduct one from the count of matches
            if second_count[i] == first_count[i] + 1:
                matches -= 1
            
            # if it added a match, increment match count
            elif second_count[i] == first_count[i]:
                matches += 1

            
            # Now, we need to remove the character from the left side of the sliding window
            k = ord(s2[j - len(s1)]) - ord('a')

            second_count[k] -= 1
            if second_count[k] + 1 == first_count[k]:
                matches -= 1
            elif second_count[k] == first_count[k]:
                matches +=1 
        
        return matches == 26
