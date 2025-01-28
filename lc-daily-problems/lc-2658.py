from typing import List


class Solution:
    def findMaxFish(self, grid: List[List[int]]) -> int: # This mfker testing my patience

        res = 0
        no_rows = len(grid)
        no_cols = len(grid[0])

        def backtrack(r, c, score):
            if r < 0 or r >= no_rows or c < 0 or c >= no_cols or grid[r][c] == 0:
                return score

            temp = grid[r][c]
            # Add current cell's fish to score immediately
            score += temp
            grid[r][c] = 0

            # Explore all directions with updated score
            score = backtrack(r - 1, c, score)  # Up
            score = backtrack(r + 1, c, score)  # Down
            score = backtrack(r, c - 1, score)  # Left
            score = backtrack(r, c + 1, score)  # Right

            grid[r][c] = temp
            return score

        for i in range(no_rows):
            for j in range(no_cols):

                if grid[i][j] != 0:

                    booyah = backtrack(i, j, 0)
                    print(f"score from row {i} col {j} = {booyah}")
                    res = max(res, booyah)

        return res


grid = [[4, 5, 5], [0, 10, 0]]
print(Solution().findMaxFish(grid))
