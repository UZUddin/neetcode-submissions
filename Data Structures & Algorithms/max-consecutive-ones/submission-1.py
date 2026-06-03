class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        count = 0
        counter = 0
        for x in range(len(nums)):
            if nums[x] == 1:
                counter += 1
            else:
                counter = 0
            if counter > count:
                count = counter
        return count