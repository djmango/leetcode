# @before-stub-for-debug-begin
from python3problem205 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=205 lang=python3
#
# [205] Isomorphic Strings
#

# @lc code=start
class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:

        mapping = {}
        # s char -> t char
        # s = foo, t = baa
        # f -> b
        # o -> a
        
        for i in range(len(s)):
            if s[i] in mapping:
                # Mapping must match if we already have it stored
                if not mapping[s[i]] == t[i]:
                    return False
            else:
                # If this is a new mapping make sure we dont already have the value stored, if not then store the mapping
                if t[i] not in mapping.values():
                    mapping[s[i]] = t[i]
                else:
                    return False
        return True
                
        
# @lc code=end

