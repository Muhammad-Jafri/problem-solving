from typing import List


class Solution:
    def waysToSplitArray(self, nums: List[int]) -> int:
        prefix_sum = []
        prefix_sum.append(nums[0])
        valid_splits = 0

        for i in range(1, len(nums)):
            prefix_sum.append(prefix_sum[i - 1] + nums[i])

        total_sum = prefix_sum[-1]

        for i in range(
            len(nums) - 1
        ):  # Looping till the second last to meat the constraint
            if (
                prefix_sum[i] >= total_sum - prefix_sum[i]
            ):  # Checking for second constraint (left sum >= right sum)
                valid_splits += 1

        return valid_splits


sol = Solution()
nums = [2, 3, 1, 0]
print(sol.waysToSplitArray(nums=nums))
