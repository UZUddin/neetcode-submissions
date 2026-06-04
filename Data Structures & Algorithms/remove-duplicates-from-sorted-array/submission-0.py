class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        x = 0
        while x+1 < len(nums):
            if nums[x] == nums[x+1]:
                nums.pop(x)
            else:
                x += 1

        return len(nums)