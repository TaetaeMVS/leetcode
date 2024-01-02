#
# @lc app=leetcode id=242 lang=python3
#
# [242] Valid Anagram
#
# https://leetcode.com/problems/valid-anagram/description/
#
# algorithms
# Easy (63.99%)
# Likes:    11503
# Dislikes: 364
# Total Accepted:    3M
# Total Submissions: 4.7M
# Testcase Example:  '"anagram"\n"nagaram"'
#
# Given two strings s and t, return true if t is an anagram of s, and false
# otherwise.
# 
# An Anagram is a word or phrase formed by rearranging the letters of a
# different word or phrase, typically using all the original letters exactly
# once.
# 
# 
# Example 1:
# Input: s = "anagram", t = "nagaram"
# Output: true
# Example 2:
# Input: s = "rat", t = "car"
# Output: false
# 
# 
# Constraints:
# 
# 
# 1 <= s.length, t.length <= 5 * 10^4
# s and t consist of lowercase English letters.
# 
# 
# 
# Follow up: What if the inputs contain Unicode characters? How would you adapt
# your solution to such a case?
# 
#

# @lc code=start
class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        char_count_s = dict()
        char_count_t = dict()
        for i in range(len(s)):
            if s[i] not in char_count_s:
                char_count_s[s[i]] = 1
            else:
                char_count_s[s[i]] += 1
            if t[i] not in char_count_t:
                char_count_t[t[i]] = 1
            else:
                char_count_t[t[i]] += 1
        for char in char_count_s:
            if char not in char_count_t:
                return False
            if char_count_s[char] != char_count_t[char]:
                return False
        return True 
    
        # Alternative solutions
        return Counter(t) == Counter(s)

        return sorted(s) == sorted(t)
    
# @lc code=end

