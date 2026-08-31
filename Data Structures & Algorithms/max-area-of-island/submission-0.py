class Solution:
    def maxAreaOfIsland(self, grid: List[List[int]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        max_area = 0

        def dfs(r, c):
            # Outside grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return 0

            # Water or already visited
            if grid[r][c] == 0:
                return 0

            # Mark as visited
            grid[r][c] = 0

            # Count current cell
            area = 1

            # Explore four directions
            area += dfs(r - 1, c)  # Up
            area += dfs(r + 1, c)  # Down
            area += dfs(r, c - 1)  # Left
            area += dfs(r, c + 1)  # Right

            return area

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == 1:
                    # Calculate this island's area
                    area = dfs(r, c)

                    # Update maximum
                    max_area = max(max_area, area)

        return max_area