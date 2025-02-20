from typing import List


class Solution:
    def tupleSameProduct(self, nums: List[int]) -> int:
        res = []

        def backtrack(cur_list, modified_nums):
            if len(cur_list) == 4:
                res.append(cur_list)
                return

            for n in modified_nums:
                backtrack(cur_list + [n], [i for i in modified_nums if i != n])

        backtrack([], nums)
        print(res)

        # n = len(nums)
        # if n < 4:
        #     return 0

        # product_count = {}
        # for i in range(n):
        #     for j in range(i+1, n):
        #         product = nums[i] * nums[j]
        #         if product in product_count:
        #             product_count[product] += 1
        #         else:
        #             product_count[product] = 1

        # result = 0
        # for product in product_count:
        #     count = product_count[product]
        #     if count > 1:
        #         result += count * (count - 1) // 2

        # return result * 8


nums = [2, 3, 4, 6]
print(Solution().tupleSameProduct(nums=nums))
