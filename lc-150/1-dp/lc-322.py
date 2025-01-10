from typing import List


class Solution:
    def coinChange(
        self, coins: List[int], amount: int
    ) -> int:  # Let's do this with recursion, commit this and then solve using dp

        res = []

        def backtrack(coins, cur_coin, no_coins, target):

            if target == 0:
                res.append(no_coins)
                return

            if target < 0:
                return

            for c in coins:
                backtrack(coins, c, no_coins + 1, target - c)

        for coin in coins:

            backtrack(coins=coins, cur_coin=coin, no_coins=0, target=amount)

        return min(res) if res != [] else -1


coins = [2]
amount = 3
print(Solution().coinChange(coins=coins, amount=amount))
