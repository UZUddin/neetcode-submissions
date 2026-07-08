class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #set up indices
        indx = {}
        for i in range(len(nums)):
            # key = nums[i]
            # value = i
            indx[nums[i]] = i

        # does y = target - x exist
        for x in range(len(nums)):
        # you have x index
            # find y
            y = target - nums[x]
            if y in indx and indx[y] != x:
                ypos = indx[y]
                return [x, ypos]

        # to find index map through key = y in nums. value = index of y
        # return index of [x], index of [y]
       