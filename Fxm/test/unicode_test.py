# -*- coding: utf-8 -*-
# Script Name   : unicode_test.py
# Author        : Caiziyang
# Created       : 2021/4/10 9:31
# Last Modified : 2021/4/10 9:31
# Version       : 1.0.1
# Modifications : 
#
# Description   :


class Solution(object):
    def findRepeatNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if len(nums) == 0:
            return -1
        for i, num in enumerate(nums):
            while nums[i] != i:
                m = nums[i]
                if nums[m] == m:
                    return m
                nums[i], nums[m] = nums[m], m
        return -1


if __name__ == '__main__':
    nums = [2, 3, 1, 5, 2, 3, 2]
    solution = Solution()
    print(solution.findRepeatNumber(nums))