class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # Iterate through the array of numbers, adding each number
         # to a set because it permits hashing
         # Then, check the remaining numbers using .in()

            # checked number set
            checked_nums = set()
            # check for duplicates
            is_dupe = False
            for num in nums:
                if num in checked_nums:
                    is_dupe = True
                    break
                checked_nums.add(num)

            return is_dupe

