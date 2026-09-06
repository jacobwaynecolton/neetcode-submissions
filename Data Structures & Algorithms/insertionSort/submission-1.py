# Definition for a pair.
# class Pair:
#     def __init__(self, key: int, value: str):
#         self.key = key
#         self.value = value
class Solution:
    def insertionSort(self, pairs: List[Pair]) -> List[List[Pair]]:

        if not pairs:
            return []

        # Creating an output list with the initial element being the list from the first iteration of the sorting process
        output_list = [pairs.copy()]
        
        # Iterating over each element of the list starting after the first
        for i in range(1,len(pairs)):
            # Using a pointer to keep track of where we are currently in our decrementation
            cur_index = i

            temp = pairs[i]

            while cur_index >= 1 and temp.key < pairs[cur_index-1].key:
                pairs[cur_index] = pairs[cur_index-1]
                cur_index -=1

            pairs[cur_index] = temp

            output_list.append(pairs.copy())
        
        return output_list
        
            
            

                



