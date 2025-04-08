from typing import List


class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        if not nums:
            return 0

        max_sum = nums[0]  # Initialize with first element
        i = 0

        while i < len(nums):
            cur_sum = nums[i]
            j = i
            k = i + 1

            while k < len(nums) and nums[k] > nums[j]:  # Need k to be in bounds
                cur_sum += nums[k]
                j += 1
                k += 1

            max_sum = max(max_sum, cur_sum)
            i = (
                j + 1
            )  # Move i to the next position after j (that would be the smaller element between j and k)

        return max_sum
