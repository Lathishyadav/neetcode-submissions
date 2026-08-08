import heapq

class MedianFinder:

    def __init__(self):
        self.small = []   # Max heap
        self.large = []   # Min heap

    def addNum(self, num: int) -> None:

        # Add to max heap
        heapq.heappush(self.small, -num)

        # Make sure every value in small <= every value in large
        if self.small and self.large and (-self.small[0] > self.large[0]):
            small_val = -heapq.heappop(self.small)
            large_val = heapq.heappop(self.large)

            heapq.heappush(self.small, -large_val)
            heapq.heappush(self.large, small_val)

        # Balance the sizes
        if len(self.small) > len(self.large) + 1:
            heapq.heappush(self.large, -heapq.heappop(self.small))

        if len(self.large) > len(self.small):
            heapq.heappush(self.small, -heapq.heappop(self.large))

    def findMedian(self) -> float:

        if len(self.small) > len(self.large):
            return float(-self.small[0])

        return (-self.small[0] + self.large[0]) / 2.0