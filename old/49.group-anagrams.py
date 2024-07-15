#
# @lc app=leetcode id=49 lang=python3
#
# [49] Group Anagrams
#
# https://leetcode.com/problems/group-anagrams/description/
#
# algorithms
# Medium (67.36%)
# Likes:    17927
# Dislikes: 537
# Total Accepted:    2.4M
# Total Submissions: 3.6M
# Testcase Example:  '["eat","tea","tan","ate","nat","bat"]'
#
# Given an array of strings strs, group the anagrams together. You can return
# the answer in any order.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: strs = ["eat","tea","tan","ate","nat","bat"]
# Output: [["bat"],["nat","tan"],["ate","eat","tea"]]
# Example 2:
# Input: strs = [""]
# Output: [[""]]
# Example 3:
# Input: strs = ["a"]
# Output: [["a"]]
# 
# 
# Constraints:
# 
# 
# 1 <= strs.length <= 10^4
# 0 <= strs[i].length <= 100
# strs[i] consists of lowercase English letters.
# 
# 
#

# @lc code=start
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        sorted_dict = {}
        for s in strs:
            sorted_str = ''.join(sorted(s))
            if sorted_str not in sorted_dict:
                sorted_dict[sorted_str] = [s]
            else:
                sorted_dict[sorted_str].append(s)
        return sorted_dict.values()
            
        
# @lc code=end

