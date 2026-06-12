class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        counter = [0 for x in range(max(nums)+1)]

        for num in nums:
            counter[num] += 1
        
        curr = 0 
        for x in range(len(counter)):
            for y in range(counter[x]):
                nums[curr] = x
                curr += 1

        print(counter)