class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        
        # Finding which array the target value is within
        target_arr = 0
        while target_arr < len(matrix) - 1 and matrix[target_arr + 1][0] <= target:
            target_arr += 1

        # Using a normal binary search inside the target array
        # to identify if the target is within it
        def binary_search(arr, target):
            if not arr:
                return False
            middle_idx = len(arr) // 2
            middle_val = arr[middle_idx]
            if target == middle_val:
                return True
            elif target > middle_val:
                return binary_search(arr[middle_idx + 1:], target)
            else:
                return binary_search(arr[:middle_idx], target)

        # Returning the binary search call on the target array
        return binary_search(matrix[target_arr], target)