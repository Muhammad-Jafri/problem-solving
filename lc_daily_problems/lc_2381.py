from typing import List


class Solution:
    def shiftingLetters(
        self, s: str, shifts: List[List[int]]
    ) -> str:  # Man i fricking love neetcode
        def digit_to_string(arr: list[int]) -> str:
            """
            Convert a list of numbers (0-25) to a string of lowercase English alphabet characters.
            """
            if not all(isinstance(num, int) and 0 <= num <= 25 for num in arr):
                raise ValueError("Input must be a list of integers between 0 and 25.")

            return "".join(chr(num + ord("a")) for num in arr)

        def shift(candidate: int, no_shifts: int):
            return (candidate + no_shifts + 26) % 26

        def string_to_digit(s: str):
            """
            Convert a string of lowercase English alphabet characters
            to a list of numbers (0-25) based on their position in the alphabet.
            """
            if not s.isalpha() or not s.islower():
                raise ValueError(
                    "Input must be a string of lowercase English alphabet characters."
                )

            return [ord(char) - ord("a") for char in s]

        int_rep = string_to_digit(s=s)
        prefix_arr = [0] * (len(s) + 1)

        for left, right, direction in reversed(shifts):
            if direction == 1:
                prefix_arr[right + 1] += 1
                prefix_arr[left] += -1

            else:
                prefix_arr[right + 1] += -1
                prefix_arr[left] += 1

        delta = prefix_arr[-1]

        for i in range(len(int_rep) - 1, -1, -1):
            int_rep[i] = shift(int_rep[i], no_shifts=delta)
            delta += prefix_arr[i]

        return digit_to_string(int_rep)


# Example usage
sol = Solution()

s = "dztz"
shifts = [[0, 0, 0], [1, 1, 1]]
print(sol.shiftingLetters(s=s, shifts=shifts))
