class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        # Using a two pointer approach
        # accounting for 1-indexing at the return statement
       lo, hi = 0, len(numbers) - 1

       while lo < hi:
            if numbers[lo] + numbers[hi] == target:
                return [lo+1,hi+1]
            elif numbers[lo] + numbers[hi] < target:
                lo += 1
            elif numbers[lo] + numbers[hi] > target:
                hi -= 1
