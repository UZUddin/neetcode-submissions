class KthLargest:

    def __init__(self, k: int, nums: List[int]):
        # nums = minHeap
        self.minHeap = nums
        #sort it automatically
        heapq.heapify(self.minHeap)
        self.k = k
        #more than k
        while len(self.minHeap) > k:
            heapq.heappop(self.minHeap)
        # now we have k elements
    def add(self, val: int) -> int:
        #add to end
        heapq.heappush(self.minHeap, val)
        #only pop if more than k
        #remove smallest bc we want k largest left
        if len(self.minHeap) > self.k:
            heapq.heappop(self.minHeap)
        #return the smallest value
        return self.minHeap[0]


