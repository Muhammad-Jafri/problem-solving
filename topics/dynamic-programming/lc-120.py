from typing import List


class Solution:
    def minimumTotal(self, triangle: List[List[int]]) -> int:
        pass

        no_rows = len(triangle)
        no_cols = len(triangle[-1])
        dp = [[0 for i in range(no_cols)] for j in range(no_rows)]
        # Init the last sublist with the last sublist of triangle and go backwards
        dp[-1] = triangle[-1]

        for i in range(no_rows - 2, -1, -1):
            for j in range(len(triangle[i])):

                dp[i][j] = triangle[i][j] + min(dp[i + 1][j], dp[i + 1][j + 1])


        return dp[0][0]
    

triangle = [[-12]]
print(Solution().minimumTotal(triangle=triangle))