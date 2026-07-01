class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        #neg bc default is minHeap
        negStones = []
        for x in stones:
            negStones.append(-x)
        self.maxHeap = negStones
        heapq.heapify(self.maxHeap)
        while len(self.maxHeap) > 1:
            #now compare top two
            one = -1 * heapq.heappop(self.maxHeap)
            two = -1 * heapq.heappop(self.maxHeap)
            if one != two:
                val = abs(one - two)
                heapq.heappush(self.maxHeap, -1 * val)
        if len(self.maxHeap) > 0:
            return (-1 * self.maxHeap[0])
        else: 
            return 0
        