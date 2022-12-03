#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start

from itertools import groupby

def string_to_consecutive_occurances(string: str) -> list:
    s = [[label, sum(1 for _ in group)] for label, group in groupby(string)]
    
    uniques = []
    for i, group in enumerate(s):
        label, count = group
        if label not in uniques:
            uniques.append(label)
            
        s[i][0] = uniques.index(label)
    
    return s
        
        

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        return string_to_consecutive_occurances(s) == string_to_consecutive_occurances(t)
        
# @lc code=end

