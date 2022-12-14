#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#
# https://leetcode.com/problems/running-sum-of-1d-array/description/
#
# @lc code=start
from typing import List


class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        
        last_sum = 0 # Store our last calculation so that we don't repeat addition operations
        
        for i, num in enumerate(nums):
            last_sum += num
            nums[i] = last_sum
            
        return nums

# @lc code=end

