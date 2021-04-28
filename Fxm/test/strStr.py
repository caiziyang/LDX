class Solution:

    def strStr(self, haystack: str, needle: str) -> int:
        L, n = len(needle), len(haystack)

        for start in range(n - L + 1):
            if haystack[start:start + L] == needle:
                return start
        return -1

    def subsets(self, nums: list[int]) -> list[list[int]]:

        n = len(nums)
        result = []

        def backtrack(start, k, route=[]):
            if len(route) == k:
                result.append(route.copy())
                return

            for i in range(start, n):
                route.append(nums[i])
                backtrack(i + 1, k)
                route.pop()

            return

        for k in range(n + 1):
            backtrack(0, k)

        return result


if __name__ == '__main__':
    haystack = [1, 2, 3, 4, 5, 6, 7, 8, 9, 5, 6, 7]
    needle = [5, 6, 7]
    nums = [1, 2]
    print(Solution().subsets(nums))