import heapq
from typing import List


def get_reverse_sorted(nums: List[int]) -> List[int]:
    min_heap = [] 
    max_heap = []
    for x in nums:
        heapq.heappush(min_heap, -x)

    while min_heap:
        max_heap.append(-heapq.heappop(min_heap))

    return max_heap




# do not modify below this line
print(get_reverse_sorted([1, 2, 3]))
print(get_reverse_sorted([5, 6, 4, 2, 7, 3, 1]))
print(get_reverse_sorted([5, 6, -4, 2, 4, 7, -3, -1]))
