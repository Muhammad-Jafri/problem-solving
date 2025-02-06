from typing import List


class Solution:
    def minPathSum(self, grid: List[List[int]]) -> int:

        no_rows = len(grid)
        no_cols = len(grid[0])
        dp = [[0 for i in range(no_cols)] for j in range(no_rows)]

        for r in range(no_rows - 1, -1, -1):
            for c in range(no_cols - 1, -1, -1):

                # Last cell
                if r == no_rows - 1 and c == no_cols - 1:
                    dp[r][c] = grid[r][c]

                # Bottom row
                elif r == no_rows - 1:

                    dp[r][c] = grid[r][c] + dp[r][c + 1]
                # Rightmost column
                elif c == no_cols - 1:
                    dp[r][c] = grid[r][c] + dp[r + 1][c]

                else:
                    dp[r][c] = grid[r][c] + min(dp[r + 1][c], dp[r][c + 1])

        return dp[0][0]


grid = [[1,2,3],[4,5,6]]
print(Solution().minPathSum(grid=grid))