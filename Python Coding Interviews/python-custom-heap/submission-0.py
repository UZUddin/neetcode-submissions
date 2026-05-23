import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    min_heap = []
    max_heap = []
    #add custom priority values
    for num in nums:
        my_tuple = (-num, num)
        heapq.heappush(min_heap, my_tuple)
    
    # pop sorted elements
    while min_heap:
        value = (heapq.heappop(min_heap))[1]
        max_heap.append(value)

    return max_heap




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
