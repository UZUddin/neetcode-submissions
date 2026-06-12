class Solution:
    def search(self, nums: List[int], target: int) -> int:
        right = len(nums)-1
        left = 0
    
        while left <= right:
            middle = (left + right) // 2
            if nums[middle] == target:
                return middle
            elif nums[left] == target:
                return left
            elif nums[right] == target:
                return right
            elif nums[middle] < target:
                left = middle + 1
            elif nums[middle] > target:
                right = middle - 1
        return -1
