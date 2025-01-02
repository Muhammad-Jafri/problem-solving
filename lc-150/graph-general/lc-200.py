from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        no_rows = len(grid)
        no_cols = len(grid[0])
        res = 0

        def backtrack(r, c):

            # Checking for boundary conditions
            if r < 0 or r >= no_rows or c < 0 or c >= no_cols or grid[r][c] == "0":
                return

            grid[r][c] = "0"

            backtrack(r - 1, c)
            backtrack(r + 1, c)
            backtrack(r, c - 1)
            backtrack(r, c + 1)

        for i in range(no_rows):
            for j in range(no_cols):

                if grid[i][j] == "1":  # Entry point
                    backtrack(i, j)
                    res += 1

        return res


grid = [
    ["1", "1", "1", "1", "0"],
    ["1", "1", "0", "1", "0"],
    ["1", "1", "0", "0", "0"],
    ["0", "0", "0", "0", "0"]
]
sol = Solution()
print(sol.numIslands(grid=grid))
