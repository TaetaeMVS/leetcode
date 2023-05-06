#
# @lc app=leetcode id=1408 lang=python3
#
# [1408] String Matching in an Array
#
# https://leetcode.com/problems/string-matching-in-an-array/description/
#
# algorithms
# Easy (63.74%)
# Likes:    752
# Dislikes: 83
# Total Accepted:    70.3K
# Total Submissions: 110.3K
# Testcase Example:  '["mass","as","hero","superhero"]'
#
# Given an array of string words, return all strings in words that is a
# substring of another word. You can return the answer in any order.
# 
# A substring is a contiguous sequence of characters within a string
# 
# 
# Example 1:
# 
# 
# Input: words = ["mass","as","hero","superhero"]
# Output: ["as","hero"]
# Explanation: "as" is substring of "mass" and "hero" is substring of
# "superhero".
# ["hero","as"] is also a valid answer.
# 
# 
# Example 2:
# 
# 
# Input: words = ["leetcode","et","code"]
# Output: ["et","code"]
# Explanation: "et", "code" are substring of "leetcode".
# 
# 
# Example 3:
# 
# 
# Input: words = ["blue","green","bu"]
# Output: []
# Explanation: No string of words is substring of another string.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= words.length <= 100
# 1 <= words[i].length <= 30
# words[i] contains only lowercase English letters.
# All the strings of words are unique.
# 
# 
#

# @lc code=start
class Solution:
    def stringMatching(self, words: List[str]) -> List[str]:
        substrings = set()
        for i in range(len(words)):
            for j in range(len(words)):
                if words[i] in words[j] and i != j:
                    substrings.add(words[i])
        return substrings
        
# @lc code=end

