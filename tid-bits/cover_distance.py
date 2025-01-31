from typing import List
from functools import lru_cache


def number_of_ways(n: int, steps: List[int]): # Instead of caching the original results, cache remaining distance instead.
    # Using lru_cache for automatic memoization
    @lru_cache(None)
    def backtrack(remaining_distance: int) -> int:
        # Base cases
        if remaining_distance == 0:
            return 1
        if remaining_distance < 0:
            return 0

        # Calculate total ways from current position
        total = 0
        for s in steps:
            total += backtrack(remaining_distance - s)

        return total

    return backtrack(n)


# Test cases
def run_tests():
    test_cases = [
        (4, [1, 2, 3]),  # Original test case
        (5, [1, 2]),  # Simple case with 2 steps
        (3, [1, 2, 3]),  # Small distance
        (7, [1, 3, 5]),  # Odd steps only
        (0, [1, 2, 3]),  # Zero distance
    ]

    for distance, available_steps in test_cases:
        result = number_of_ways(distance, available_steps)
        print(f"Distance: {distance}, Steps: {available_steps}, Ways: {result}")


# Run the tests
run_tests()


# from typing import List # Brute force implementation


# def number_of_ways(n: int, steps: List[int]):

#     res = 0

#     def backtrack(remaining_distance):
#         nonlocal res
#         if remaining_distance == 0:
#             res += 1
#             return

#         if remaining_distance < 0:
#             return

#         for s in steps:
#             backtrack(remaining_distance - s)

#     backtrack(n)
#     return res


# n = 4
# steps = [1, 2, 3]
# print(number_of_ways(n=n, steps=steps))
