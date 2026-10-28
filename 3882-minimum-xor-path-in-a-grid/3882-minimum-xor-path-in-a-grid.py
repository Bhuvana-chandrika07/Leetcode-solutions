class Solution:
    def minCost(self, grid: List[List[int]]) -> int:
        m, n = len(grid), len(grid[0])
        # dp[j] stores a set of possible XOR values reaching column j
        dp = [set() for _ in range(n)]
        
        dp[0].add(0)
        
        for i in range(m):
            new_dp = [set() for _ in range(n)]
            for j in range(n):
                # Values coming from top cell (i - 1, j)
                if i > 0:
                    for val in dp[j]:
                        new_dp[j].add(val ^ grid[i][j])
                # Values coming from left cell (i, j - 1)
                if j > 0:
                    for val in new_dp[j - 1]:
                        new_dp[j].add(val ^ grid[i][j])
                # Special case for the starting cell (0, 0)
                if i == 0 and j == 0:
                    new_dp[0].add(grid[0][0])
            dp = new_dp
            
        return min(dp[n - 1])
