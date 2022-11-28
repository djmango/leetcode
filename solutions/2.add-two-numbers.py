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
import copy


class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        numbers = []

        # First we want to assemble the linked list into an operable number (I know you can do this in 1 pass but this is easier to understand)
        for listnode in (l1, l2):
            assembled_number = 0

            # Traverse the listnode down, starting with the smallest digit
            i = 0
            while listnode:
                assembled_number += (listnode.val * (10**i)) # Construct an assembled number from the digits, multiplying by 10^i
                i += 1
                listnode = listnode.next

            numbers.append(assembled_number)

        summed = sum(numbers)
        sum_list = [int(d) for d in str(summed)]

        # We can now assembled the linked list, starting with the last link as the largest digit
        returned_listnode = None 
        while len(sum_list) != 0:
            num = sum_list.pop(0)
            returned_listnode = ListNode(num, copy.deepcopy(returned_listnode))

        return returned_listnode

# @lc code=end

