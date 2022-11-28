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
import copy


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        num1 = 0
        num2 = 0

        for listnode, assembled_number in ((l1, num1), (l2, num2)):
            zeropad = 1
            while listnode:
                if zeropad == 0: zeropad = 1
                assembled_number += (listnode.val * zeropad)
                zeropad *= 10
                listnode = listnode.next
        
        sum = num1 + num2
        sum_list = [int(d) for d in str(sum)]

        returned_listnode = None 
        while len(sum_list) != 0:
            num = sum_list.pop(0)
            returned_listnode = ListNode(num, copy.deepcopy(returned_listnode))
            print(returned_listnode)
        
        print(returned_listnode)
        return returned_listnode

# @lc code=end

