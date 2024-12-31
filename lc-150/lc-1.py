from typing import List


class Solution:

    def twoSum(self, nums: List[int], target: int) -> List[int]:

        hashmap = {}  # nums[i] + nums[j] = target
                      # nums[j] = target - nums[i]

        for i in range(len(nums)):

            complement = target - nums[i]
            if complement in hashmap.keys():
                j = hashmap[complement]
                return [j, i]

            hashmap[nums[i]] = i

        return []


nums = [3, 2, 4]
target = 6
sol = Solution()
print(sol.twoSum(nums=nums, target=target))
