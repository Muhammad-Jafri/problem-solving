from typing import List


class Solution:
    def longestMonotonicSubarray(self, nums: List[int]) -> int:  # Need to revisit
        i = 0
        max_seq = 0

        while i < len(nums) - 1:
            if nums[i + 1] > nums[i]:  # Entry point
                j = i + 1
                k = i

                while nums[j] > nums[k]:
                    k += 1
                    j += 1

                print(f"right most index {j}")
                print(f"left most index {j}")
                max_seq = max(max_seq, j - i)

            i += 1

        return max_seq


nums = [0, 2, 4, 3]

print(Solution().longestMonotonicSubarray(nums))
