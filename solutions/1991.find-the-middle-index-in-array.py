#
# @lc app=leetcode id=1991 lang=python3
#
# [1991] Find the Middle Index in Array
#

# @lc code=start
class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
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

