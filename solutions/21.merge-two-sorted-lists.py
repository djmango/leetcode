#
# @lc app=leetcode id=21 lang=python3
#
# [21] Merge Two Sorted Lists
#

# @lc code=start
# Definition for singly-linked list.
from typing import Optional


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next

class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        listnode_root = n = ListNode(0)
        
        # Sort non-dereasing 
        while list1 or list2:
            if list1 and list2:
                if list1.val <= list2.val:
                    n.val = list1.val
                    n.next = ListNode(list2.val)
                else:
                    n.val = list2.val
                    n.next = ListNode(list1.val)

            elif list1:
                n.val = list1.val
            elif list2:
                n.val = list2.val
            
            n = n.next
            list1 = list1.next
            list2 = list2.next
        
        return listnode_root
        
# @lc code=end

