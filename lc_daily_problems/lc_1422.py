class Solution:
    def maxScore(
        self, s: str
    ) -> int:  # TODO this shit works but brute force AF, optimize it with a fresh mind
        def score_lhs(s: str):
            res = 0

            for digit in s:
                if digit == "0":
                    res += 1

            return res

        def score_rhs(s: str):
            res = 0

            for digit in s:
                if digit == "1":
                    res += 1

            return res

        max_score = 0

        for i in range(len(s) - 1):
            left_sublist = s[0 : i + 1]
            right_sublist = s[i + 1 :]
            print(
                f"iteration {i}, left sublist : {left_sublist}, right sublist : {right_sublist}"
            )
            max_score = max(
                max_score, score_lhs(left_sublist) + score_rhs(right_sublist)
            )

        return max_score


sol = Solution()
s = "1111"
print(sol.maxScore(s=s))
