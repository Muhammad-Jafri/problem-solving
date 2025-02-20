from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = []
        n = len(nums)

        def backtrack(idx, cur):
            if idx >= n:
                res.append(cur)
                return

            # Include the element
            backtrack(idx + 1, cur + [nums[idx]])
            # Not include the element
            backtrack(idx + 1, cur)

        backtrack(0, [])
        return res


test = [1, 2, 3]
print(Solution().subsets(nums=test))
