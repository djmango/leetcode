# @before-stub-for-debug-begin
from python3problem451 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=451 lang=python3
#
# [451] Sort Characters By Frequency
#

# @lc code=start
from collections import Counter

class Solution:
    def frequencySort(self, s: str) -> str:
        counted = Counter(s)
        return ''.join([k*v for k, v in sorted(counted.items(), key=lambda item: item[1], reverse=True)])
        
# @lc code=end

