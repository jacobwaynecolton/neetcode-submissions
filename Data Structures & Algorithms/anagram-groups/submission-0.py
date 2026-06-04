class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        # Solving using a hashmap / dictionary.
        # Using the ASCII codes and ord() to create a frequency
        # array to utilize as keys in the dictionary 
        seen_words = {}
        for word in strs:
            frequency = [0] * 26
            for letter in word: 
                frequency[ord(letter) - ord('a')] += 1
            
            # Making the frequency hashable
            tup_frequency = tuple(frequency)
            
            if tup_frequency in seen_words:
                seen_words[tup_frequency].append(word)
            else:
                seen_words[tup_frequency] = [word]
        return list(seen_words.values())