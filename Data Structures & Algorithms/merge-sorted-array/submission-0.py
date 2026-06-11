class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        #add nums2 to the end of nums1
        for x in range(n): 
            nums1[m + x] = nums2[x]
        
        #insertion sort of m elements
        #starts
        for y in range(m, m+n):
            #while previous is more, switch.
            t = y
            while t>0 and nums1[t-1] >= nums1[t]:
                prev = nums1[t-1] 
                nums1[t-1] = nums1[t]
                nums1[t] = prev
                t -= 1
            
        print(nums1)
        print(nums2)