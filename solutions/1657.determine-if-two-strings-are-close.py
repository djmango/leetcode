#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

from collections import Counter

# @lc code=start

def string_to_occurances(string: str) -> list:
    return Counter(string).values()

def string_unique_letters(string: str) -> set:
    return set(string)

class Solution:

    def closeStrings(self, word1: str, word2: str) -> bool:
        # They of course need to be the same length as neither of the allowed operations changes the length of the string
        if len(word1) != len(word2):
            return False
        
        # We also need to make sure the occurances of characters match up, but they don't need to be the same character, only the count
        # For example, "bbaaac" counts match up with "aacccb".
        # This works because the second operation allows us to swap the occurances of any two characters
        word1_letter_occurances = string_to_occurances(word1) 
        word2_letter_occurances = string_to_occurances(word2)
        
        # These conditions validate if the strings are close, no need to do the actual operation
        return (sorted(word1_letter_occurances) == sorted(word2_letter_occurances)) and (set(word1) == set(word2))
        
# @lc code=end

