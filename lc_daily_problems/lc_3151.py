from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        is_special = True
        n = len(nums)

        if n == 1:
            return is_special

        for i in range(n - 1):
            if nums[i] % 2 == nums[i + 1] % 2:
                is_special = False
                break

        return is_special


nums = [4, 3, 2, 11]
print(Solution().isArraySpecial(nums=nums))
