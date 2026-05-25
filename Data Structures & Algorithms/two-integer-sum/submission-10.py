class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for i, num in enumerate(nums):

            for j in range(i+1, len(nums)):
                # check if it's not in seen, if not, add it 
                if nums[j] not in seen or (nums[j] in seen and seen[nums[j]] != j):
                    seen[nums[j]] = j

                    if num + nums[j] == target:
                        return [i, j]
                else:
                    if seen[nums[j]] > i:
                        print('here')
                        print(f"target = {target}, num = {num}, nums[j] = {nums[j]}, target - num = {target-num}")
                        if target - num == nums[j]:
                            print('now here')
                            print(i,seen[nums[j]])
                            return [i, seen[nums[j]]]