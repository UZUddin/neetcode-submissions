class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        #set up indices
        indx = {}
        for i in range(len(nums)):
            indx[nums[i]] = i

        for x in range(len(nums)):
            # calc value
            y = target - nums[x]
            if y in indx and indx[y] != x:
                #find y
                ypos = indx[y]
                # return index of [x], index of [y]
                return [x, ypos]

       