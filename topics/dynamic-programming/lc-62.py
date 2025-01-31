from pprint import pprint


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:

        dp = [[0 for i in range(n)] for j in range(m)]
        pprint(dp)
        for i in range(m - 1, -1, -1):  # Rows
            for j in range(n - 1, -1, -1):  # Cols

                # Check if the robot is to the right or to the bottom
                if i == m - 1 or j == n - 1:

                    dp[i][j] = 1

                else:
                    dp[i][j] = dp[i + 1][j] + dp[i][j + 1]

        return dp[0][0]


m = 3
n = 7
print(Solution().uniquePaths(m=m, n=n))
