class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
         # Iterate through the array of numbers, adding each number
         # to a set because it permits hashing
         # Then, check the remaining numbers using .in()

            # checked number set
            checked_nums = set()
            for num in nums:
                if num in checked_nums:
                    return True
                checked_nums.add(num)

            return False

