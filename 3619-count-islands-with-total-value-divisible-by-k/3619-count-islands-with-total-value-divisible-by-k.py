class Solution:
    def dfs(self, i, j, n, m, grid):
        if i < 0 or i >= n or j < 0 or j >= m:
            return 0

        if grid[i][j] == 0:
            return 0

        total = grid[i][j]
        grid[i][j] = 0

        total += self.dfs(i, j - 1, n, m, grid)
        total += self.dfs(i, j + 1, n, m, grid)
        total += self.dfs(i - 1, j, n, m, grid)
        total += self.dfs(i + 1, j, n, m, grid)

        return total

    def countIslands(self, grid, k):
        n = len(grid)
        m = len(grid[0])
        count = 0

        for i in range(n):
            for j in range(m):
                if grid[i][j] > 0:
                    total = self.dfs(i, j, n, m, grid)
                    if total % k == 0:
                        count += 1

        return count