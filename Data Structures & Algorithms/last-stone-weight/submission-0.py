class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:
        '''
        we always want the top 2 heaviest stones
        max heap
            make sure to do the negative stuff to invert it whenever we operate
            add all nums --> heapify

        iterate till only one stone is left
        while len(heap) > 1
            pop top 2 
            subtract them
            push back onto heap
        return heap[0]
        '''
        maxHeap = [-n for n in stones]
        heapq.heapify(maxHeap)
        while len(maxHeap) > 1:
            stone1 = -heapq.heappop(maxHeap)
            stone2 = -heapq.heappop(maxHeap)
            heapq.heappush(maxHeap, stone2-stone1)
        return -maxHeap[0]