#
# @lc app=leetcode id=724 lang=python3
#
# [724] Find Pivot Index
#

# @lc code=start
from typing import List


class Solution:
    def pivotIndex(self, nums: List[int]) -> int:

        if nums is None or len(nums) == 0:
            return -1

        left = 0
        mid = 0
        right = sum(nums)

        for i in range(len(nums)):
            left += mid
            mid = nums[i]
            right -= nums[i]
            if left == right:
                return i

        return -1

# @lc code=end
