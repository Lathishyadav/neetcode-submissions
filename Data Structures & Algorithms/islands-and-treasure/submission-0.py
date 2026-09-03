class Solution:
    def islandsAndTreasure(self, grid: List[List[int]]) -> None:

        from collections import deque

        rows = len(grid)
        cols = len(grid[0])

        queue = deque()

        # Add all treasure chests to the queue
        for r in range(rows):
            for c in range(cols):
                if grid[r][c] == 0:
                    queue.append((r, c))

        # BFS from all treasure chests
        while queue:

            r, c = queue.popleft()

            directions = [
                (-1, 0),  # up
                (1, 0),   # down
                (0, -1),  # left
                (0, 1)    # right
            ]

            for dr, dc in directions:
                nr = r + dr
                nc = c + dc

                # Valid land cell
                if (0 <= nr < rows and
                    0 <= nc < cols and
                    grid[nr][nc] == 2147483647):

                    # Distance = current distance + 1
                    grid[nr][nc] = grid[r][c] + 1

                    queue.append((nr, nc))