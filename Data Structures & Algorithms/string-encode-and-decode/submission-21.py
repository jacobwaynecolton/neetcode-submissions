class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # Checking if strs is empty
        if not strs:
            return ""
        
        # The final string
        final_str = "" 

        # Iterating through each string in the list
        # and for each string, append its length, separate the 
        # lengths by x's
        for string in strs:
            final_str += "x" + str(len(string))

        # Prepend the length of the portion which clarifies
        # the lengths of the strings
        # then append the actual strings themselves on to the end
        final_str = str(len(final_str)) + final_str
        final_str += "x" + ''.join(strs)

        return final_str

    def decode(self, s: str) -> List[str]:
        # If the string is empty, return an empty list
        if not s:
            return []
        # Isolating the initial stats (the string of all the string lengths)
        initial_stats_len = s.index('x')
        initial_stats = int(s[:initial_stats_len])
        # Creating a list for the final strings to return
        strings = []
        # Breaking up initial stats per item 
        string_lengths = s[initial_stats_len + 1 : initial_stats_len + initial_stats].split('x')
        # Separating the final strings as one string
        string_values = s[initial_stats + 1 + initial_stats_len:]

        # Keeping track of the current positioning in the values string
        cur_str_pos = 0
        # For each string length
        for length in string_lengths:
            # append the string from the current string position to the current position +
            # the length of the current string
            strings.append(string_values[cur_str_pos:cur_str_pos + int(length)])
            # Increment the string position pointer
            cur_str_pos += int(length)
            
        return strings
