# @before-stub-for-debug-begin
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

        assert len(profits) == len(capital), "Somehow the profits and capital lists don't match in length"

        # First we want to assemble a list of nice to use project tuples, as defined below

        # project: (index, profit, capital, completed)

        # projects[project]
        projects = [(i, project[0], project[1], False) for i, project in enumerate(zip(profits, capital))]
        
        projects.sort(key=lambda project: project[1], reverse=True)

        # Now we have to assemble a k-length list of the best projects we can afford

        # We track out capital in total_capital, and run the following k-times to get the max back
        total_capital = w
        for i in range(k):
            # So here we assemble a list of projects we can afford and have not completed
            affordable_projects = filter(lambda project: project[2] <= total_capital and not project[3], projects)
            
            try:
                best_project = next(affordable_projects)
            except Exception:
                break
            
            # Calculate and store our profit
            total_capital += best_project[1]
            
            # Mark that we completed the project
            projects[projects.index(best_project)] = (best_project[0], best_project[1], best_project[2], True)
            
        return total_capital

# @lc code=end
