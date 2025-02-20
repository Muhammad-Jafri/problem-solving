from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        hashmap = {}  # nums[i] + nums[j] = target
        # nums[j] = target - nums[i]

        for i in range(len(nums)):
            complement = nums[i]
            if complement in hashmap.keys():
                j = hashmap[complement]
                if abs(i - j) <= k:
                    return True

            hashmap[nums[i]] = i

        return False


nums = [1, 2, 3, 1, 2, 3]
k = 2
sol = Solution()
print(sol.containsNearbyDuplicate(nums, k))
