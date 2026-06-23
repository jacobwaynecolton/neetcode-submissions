class Solution:

    def encode(self, strs: List[str]) -> str:
        # The final string
        final_str = "" 

        # Iterating through each string in the list
        for string in strs:
            final_str += "x" + str(len(string))
        final_str = str(len(final_str)) + final_str
        final_str += "x" + ''.join(strs)

        return final_str

    def decode(self, s: str) -> List[str]:
        if s[0] == '0':
            return []
        # First removing the initial stats
        initial_stats_len = 0
        for char in s:
            if char != 'x':
                initial_stats_len += 1
            else:
                break

        initial_stats = int(s[:initial_stats_len])
        strings = []
        # Breaking up initial stats per item 
        string_lengths = s[initial_stats_len+1:initial_stats_len +  initial_stats].split('x')
        string_values = s[initial_stats + 1 + initial_stats_len:]


        for length in string_lengths:
            strings.append(string_values[:int(length)])
            string_values = string_values[int(length):]
        return strings
