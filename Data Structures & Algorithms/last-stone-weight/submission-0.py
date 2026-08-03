import heapq

class Solution:
    def lastStoneWeight(self, stones: List[int]) -> int:

        # Create a max-heap using negative values
        heap = [-stone for stone in stones]
        heapq.heapify(heap)

        while len(heap) > 1:
            y = -heapq.heappop(heap)  # Heaviest
            x = -heapq.heappop(heap)  # Second heaviest

            if y != x:
                heapq.heappush(heap, -(y - x))

        return -heap[0] if heap else 0