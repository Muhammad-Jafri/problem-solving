from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
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


# Test
coins = [2]
amount = 3
print(Solution().coinChange(coins=coins, amount=amount))
