class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        ### Thoughts : 
        # Aim for O(n) and O(m) complexity where m is the number of unique characters in the string
        # presumably, the idea here is to continue off from the point in your current longest sequence
        # from where the character which broke it last was, so we would need to keep track of where
        # the indices are for each of the current unique characters 
        # maybe create a dictionary with each unique character and their current furthest index? 
        # as well as keep track of the current highest total sequence length 
        
        # update the current max length by subtracting the current length by the length of the character
        # which broke the streak

        # Ah, but we only need to know about the positioning of each unique character, if that unique
        # character comes AFTER the current left bound. Otherwise it's part of a purged string

        # keeping track of the current cut-off point in the string, as well as the max sequence length
        # current sequence length, and a dictionary of the most up do date indices for each character
        # as we traverse left to right
        cur_char_i = {}
        max_str_len = 0
        cur_str_len = 0
        cur_cutoff = 0

        for i, char in enumerate(s):

            # If the character not in the dictionary which tracks up-to-date indices, add
            if char not in cur_char_i:
                cur_char_i[char] = i
                cur_str_len += 1 
            # If the character is in the dictionary, and it is past the cutoff, you have hit a new duplicate, purge part of the string and update the cutoff point for the purge
            elif cur_char_i[char] >= cur_cutoff:
                cur_str_len = i - cur_char_i[char]
                cur_cutoff = cur_char_i[char] + 1
                cur_char_i[char] = i
            # If the character is in the dictionary, but is prior to the cutoff point, it is an irrelevant duplication, because that original character is removed during the earlier purging 
            else:
                cur_str_len += 1
                cur_char_i[char] = i

            # Update the max str length to be the larger of the max and current lengths
            max_str_len = max(max_str_len,cur_str_len)
            
        return max_str_len



