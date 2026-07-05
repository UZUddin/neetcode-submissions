class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        my_hashset = set()

        for n in nums:
            if n in my_hashset:
                return True
            else:
                my_hashset.add(n)
     
        return False
    