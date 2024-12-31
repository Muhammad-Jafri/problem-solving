class Solution:
    def isHappy(self, n: int) -> bool:

        def sum_of_squares(nums: list):
            squared_list = map(lambda x: x ** 2, nums)
            return sum(squared_list)

        def convert_num_to_digits(n: int) -> list[int]:
            return [int(digit) for digit in str(n)]

        hashmap = {}
        hashmap[n] = 1

        while True:

            computed_num = sum_of_squares(convert_num_to_digits(n))

            if computed_num == 1:
                return True

            if computed_num in hashmap.keys():
                return False

            hashmap[computed_num] = 1
            n = computed_num


n = 19
sol = Solution()
print(sol.isHappy(n=n))
