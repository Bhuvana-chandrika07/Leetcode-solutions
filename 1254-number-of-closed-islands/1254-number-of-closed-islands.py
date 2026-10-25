class Solution:
    def closedIsland(self, grid: list[list[int]]) -> int:
        n, m = len(grid), len(grid[0])
        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]

        def convert(i, j, target):
            # Mark every land cell connected to the current cell
            for dx, dy in directions:
                x, y = i + dx, j + dy

                if 0 <= x < n and 0 <= y < m and grid[x][y] == 0:
                    grid[x][y] = target
                    convert(x, y, target)

            return

        # Mark islands connected to the left and right boundaries
        for i in range(n):
            if grid[i][0] == 0:
                grid[i][0] = 2
                convert(i, 0, 2)

            if grid[i][m-1] == 0:
                grid[i][m-1] = 2
                convert(i, m-1, 2)

        # Mark islands connected to the top and bottom boundaries
        for j in range(m):
            if grid[0][j] == 0:
                grid[0][j] = 2
                convert(0, j, 2)

            if grid[n-1][j] == 0:
                grid[n-1][j] = 2
                convert(n-1, j, 2)

        res = 0

        # Every remaining island is closed
        for i in range(1, n-1):
            for j in range(1, m-1):
                if grid[i][j] == 0:
                    res += 1

                    # Mark the entire island so we count it only once
                    grid[i][j] = 2
                    convert(i, j, 2)

        return res