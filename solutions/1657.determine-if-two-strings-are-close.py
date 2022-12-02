#
# @lc app=leetcode id=1657 lang=python3
#
# [1657] Determine if Two Strings Are Close
#

from collections import Counter

# @lc code=start

def string_to_occurances(string: str) -> list:
    letters = list(string)
    return Counter(letters).values()

def string_unique_letters(string: str) -> set:
    return set(list(string))

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
        
        # https://stackoverflow.com/questions/7828867/how-to-efficiently-compare-two-unordered-lists-not-sets
        if Counter(word1_letter_occurances) != Counter(word2_letter_occurances):
            return False
        
        # All the letters of each have to be in the other
        if string_unique_letters(word1) != string_unique_letters(word2):
            return False
        
        # Now as far as I'm aware, these should be solvable. Actually now that I'm thinking about it, we don't even
        # need to do the operation if these rules are correct, we can just return true
        return True
        
        
# @lc code=end

