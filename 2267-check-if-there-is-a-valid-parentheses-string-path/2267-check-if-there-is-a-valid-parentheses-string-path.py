class Solution:
    def hasValidPath(self, grid: list[list[str]]) -> bool:
        m, n = len(grid), len(grid[0])

        # A valid parentheses string must have an even length
        if (m + n - 1) % 2 != 0:
            return False
        # Must start with '(' and end with ')'
        if grid[0][0] == ')' or grid[m - 1][n - 1] == '(':
            return False

        from functools import cache

        @cache
        def dfs(r: int, c: int, balance: int) -> bool:
            # Update balance for current cell
            balance += 1 if grid[r][c] == '(' else -1

            # Too many closing brackets
            if balance < 0:
                return False

            # Remaining steps cannot satisfy the remaining open brackets
            remaining_steps = (m - 1 - r) + (n - 1 - c)
            if balance > remaining_steps:
                return False

            # Destination reached
            if r == m - 1 and c == n - 1:
                return balance == 0

            # Explore right and down
            if r + 1 < m and dfs(r + 1, c, balance):
                return True
            if c + 1 < n and dfs(r, c + 1, balance):
                return True

            return False

        return dfs(0, 0, 0)
        