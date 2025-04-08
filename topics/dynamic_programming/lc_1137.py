from collections import defaultdict


class Solution:
    def tribonacci(self, n: int) -> int:
        has_cache = defaultdict(bool)
        cache_val = defaultdict(int)

        def recursive_sol(n):
            if n == 0:
                return 0
            if n == 1 or n == 2:
                return 1

            if has_cache[n]:
                return cache_val[n]

            cache_val[n] = (
                recursive_sol(n - 1) + recursive_sol(n - 2) + recursive_sol(n - 3)
            )
            has_cache[n] = True

            return cache_val[n]

        return recursive_sol(n)
