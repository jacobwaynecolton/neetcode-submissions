class Solution:

    def encode(self, strs: List[str]) -> str:
        
        # Checking if strs is empty
        if not strs:
            return ""
        
        # The final string
        final_str = "" 

        # Iterating through each string in the list
        for string in strs:
            final_str += "x" + str(len(string))
        final_str = str(len(final_str)) + final_str
        final_str += "x" + ''.join(strs)

        return final_str

    def decode(self, s: str) -> List[str]:
        if not s:
            return []
        # First removing the initial stats
        initial_stats_len = s.index('x')

        initial_stats = int(s[:initial_stats_len])
        strings = []
        # Breaking up initial stats per item 
        string_lengths = s[initial_stats_len+1:initial_stats_len +  initial_stats].split('x')
        string_values = s[initial_stats + 1 + initial_stats_len:]

        cur_str_pos = 0
        for length in string_lengths:
            strings.append(string_values[cur_str_pos:cur_str_pos + int(length)])
            cur_str_pos += int(length)
        return strings
