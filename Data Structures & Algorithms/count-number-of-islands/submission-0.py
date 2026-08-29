class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        rows = len(grid)
        cols = len(grid[0])
        islands = 0

        def dfs(r, c):
            # Outside the grid
            if r < 0 or r >= rows or c < 0 or c >= cols:
                return

            # Water or already visited
            if grid[r][c] == "0":
                return

            # Mark as visited
            grid[r][c] = "0"

            # Up
            dfs(r - 1, c)

            # Down
            dfs(r + 1, c)

            # Left
            dfs(r, c - 1)

            # Right
            dfs(r, c + 1)

        for r in range(rows):
            for c in range(cols):

                if grid[r][c] == "1":
                    # Found a new island
                    islands += 1

                    # Visit the complete island
                    dfs(r, c)

        return islands