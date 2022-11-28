# @before-stub-for-debug-begin
from python3problem2 import *
from typing import *
# @before-stub-for-debug-end

#
# @lc app=leetcode id=2 lang=python3
#
# [2] Add Two Numbers
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
from typing import List, Optional


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        bump = 0
        listnode_root = n = ListNode(0)

        while l1 or l2 or bump:
            if not l1:
                l1 = ListNode(0, None)
            if not l2:
                l2 = ListNode(0, None)

            val = l1.val + l2.val + bump
            bump, val = divmod(val, 10)

            n.next = ListNode(val) 

            n = n.next
            l1 = l1.next
            l2 = l2.next
        
        return listnode_root.next

# @lc code=end

