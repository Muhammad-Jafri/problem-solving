from typing import List


class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:

        is_special = True
        n = len(nums)

        if n == 1:
            return is_special

        for i in range(n - 1):

            if (nums[i] % 2 == 0 and nums[i + 1] % 2 == 0) or (
                nums[i] % 2 == 1 and nums[i + 1] % 2 == 1
            ):

                is_special = False
                break

        return is_special


nums = [4,3,1,6]
print(Solution().isArraySpecial(nums=nums))