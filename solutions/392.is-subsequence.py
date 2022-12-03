# @before-stub-for-debug-begin
from python3problem392 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=392 lang=python3
#
# [392] Is Subsequence
#

# @lc code=start
class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        for char in s:
            if char in t:
                t = t[t.index(char)+1:]
            else:
                return False
        
        return True

        
# @lc code=end

