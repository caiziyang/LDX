
class Solution(object):

    def __init__(self):
        self.pre_sum = 0
        self.left_sum = 0
        self.count = 0

    def pivot_index(self, nums: list):
        # 数组的和
        for x in nums:
           self.pre_sum += x

        for index, valus in enumerate(nums):
            # 发现相同情况
            if self.left_sum == self.presum - valus - self.left_sum:
                return index
            self.left_sum += nums[index]

        return -1

    def sub_array_sum(self, nums, k):
        for i, v in enumerate(nums):
            try:
                if k - nums[i] == nums[i+1]:
                    self.count += 1
            except IndexError:
                ...
            # for j in range(i, len(nums)):
            #     self.sum += nums[j]
            #     if self.sum == k:
            #         self.count += 1
            # self.sum = 0
        return self.count


if __name__ == '__main__':
    nums = [2,2,2,2,2,2,2,2]
    solution = Solution()
    print(solution.sub_array_sum(nums, 4))
