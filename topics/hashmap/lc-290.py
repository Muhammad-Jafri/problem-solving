from collections import defaultdict


class Solution:
    def wordPattern(
        self, pattern: str, s: str
    ) -> bool:  # TODO the solution is not OPTIMAL
        hashmap_p = defaultdict(int)
        hashmap_str = defaultdict(int)

        for char in pattern:  # Populate pattern hashmap
            hashmap_p[char] += 1

        for word in s.split():  # Populate s's hashmap
            hashmap_str[word] += 1

        p_values = list(hashmap_p.values())
        str_values = list(hashmap_str.values())
        print(p_values)
        print(str_values)

        if sorted(p_values) == sorted(str_values):
            return True

        return False


pattern = "abba"
s = "dog cat cat fish"
sol = Solution()
print(sol.wordPattern(pattern=pattern, s=s))
