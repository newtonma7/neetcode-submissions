class KthLargest:
    '''
    use a heap
        heap automatically sorts itself as we insert, so we add to the heap and then pop k times
    '''
    def __init__(self, k: int, nums: List[int]):
        self.heap = nums
        heapq.heapify(self.heap)
        self.kth = k
        while len(self.heap) > k:
            heapq.heappop(self.heap)

    def add(self, val: int) -> int:
        heapq.heappush(self.heap, val)
        if len(self.heap) > self.kth:
            heapq.heappop(self.heap)
        return self.heap[0]
