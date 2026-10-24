class Solution {
    private int dfs(
        int i, int j, int m, int n, String word1, String word2, int[][] memo
    ) {
        if (i == 0) return j;
        if (j == 0) return i;
        if (memo[i][j] != 0) return memo[i][j];
        if (word1.charAt(i - 1) == word2.charAt(j - 1)) {
            memo[i][j] = dfs(i - 1, j - 1, m, n, word1, word2, memo);
        } else {
            memo[i][j] = Math.min(
                1 + dfs(i - 1, j, m, n, word1, word2, memo),
                1 + dfs(i, j - 1, m, n, word1, word2, memo)
            );
        }
        return memo[i][j];
    }

    public int minDistance(String word1, String word2) {
        // Top-down
        // int m = word1.length();
        // int n = word2.length();
        // int[][] memo = new int[m+1][n+1];
        // return dfs(m, n, m, n, word1, word2, memo);

        // // Bottom-up 2D
        // int m = word1.length();
        // int n = word2.length();
        // int[][] dp = new int[m+1][n+1];
        // for (int i = 0; i <= m; ++i) {
        //     dp[i][0] = i;
        // }
        // for (int j = 0; j <= n; ++j) {
        //     dp[0][j] = j;
        // }

        // for (int i = 1; i <= m; ++i) {
        //     for (int j = 1; j <= n; ++j) {
        //         if (word1.charAt(i-1)==word2.charAt(j-1)) {
        //             dp[i][j] = dp[i-1][j-1];
        //         } else {
        //             dp[i][j] = Math.min(
        //                 dp[i-1][j] + 1,
        //                 dp[i][j-1] + 1
        //             );
        //         }
        //     }
        // }
        // return dp[m][n];


        // Bottom-up 1D + prevDiag
        int m = word1.length();
        int n = word2.length();
        int[] dp = new int[n+1];
        for (int j = 1; j <= n; ++j) {
            dp[j] = j;
        }
        for (int i = 1; i <= m; ++i) {
            int prevDiag = dp[0];
            dp[0] = i;
            for (int j = 1; j <= n; ++j) {
                int temp = dp[j];
                if (word1.charAt(i-1)==word2.charAt(j-1)) {
                    dp[j] = prevDiag;
                } else {
                    dp[j] = Math.min(
                        dp[j-1] + 1,
                        dp[j] + 1
                    );
                }
                prevDiag = temp;
            }
        }
        return dp[n];
    }
}