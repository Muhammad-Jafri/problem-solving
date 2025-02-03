from typing import List
from math import ceil, sqrt

class Solution:
    def numSquares(self, n: int) -> int:

        def coinChange(coins: List[int], amount: int) -> int:
            # Create cache dictionary
            cache = {}

            def backtrack(target):
                # Base cases
                if target == 0:
                    return 0
                if target < 0:
                    return float("inf")
                # Check cache
                if target in cache:
                    return cache[target]

                # Try each coin and get minimum
                min_coins = float("inf")
                for coin in coins:
                    result = backtrack(target - coin)
                    if result != float("inf"):
                        min_coins = min(min_coins, result + 1)

                # Store in cache and return
                cache[target] = min_coins
                return min_coins

            result = backtrack(amount)
            return result if result != float("inf") else -1
        
        squared_list = [i ** 2 for i in range(1, ceil(sqrt(n)) + 1)]
        print(squared_list)
        return coinChange(squared_list, n)


n = 4
print(Solution().numSquares(n = n))
