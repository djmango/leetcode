# @before-stub-for-debug-begin
from heapq import heappop, heappush
from python3problem502 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=502 lang=python3
#
# [502] IPO
#

# @lc code=start
from typing import List


class Solution:
    def findMaximizedCapital(self, k: int, w: int, profits: List[int], capital: List[int]) -> int:
        # First we want to assemble a list of nice to use projects, and sort by capital
        projects = list(zip(capital, profits))
        projects.sort()

        queue = []
        ptr = 0
        n = len(profits)
        for i in range(k):
            while ptr < n and projects[ptr][0] <= w:
                heappush(queue, -projects[ptr][1])
                ptr += 1
            if not queue:
                break
            w += -heappop(queue)
        return w

# @lc code=end
