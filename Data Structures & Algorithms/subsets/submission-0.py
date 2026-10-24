class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        seen = set()
        cur_list = [[]]
        for num in nums:
            if num not in seen:
                for i in range(len(cur_list)):
                    if cur_list[i]:
                        num_list_copy = cur_list[i].copy()
                        num_list_copy.append(num)
                        cur_list.append(num_list_copy)
                cur_list.append([num])
                seen.add(num)
        return cur_list