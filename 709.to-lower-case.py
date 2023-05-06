#
# @lc app=leetcode id=709 lang=python3
#
# [709] To Lower Case
#
# https://leetcode.com/problems/to-lower-case/description/
#
# algorithms
# Easy (82.43%)
# Likes:    1551
# Dislikes: 2615
# Total Accepted:    420.4K
# Total Submissions: 510K
# Testcase Example:  '"Hello"'
#
# Given a string s, return the string after replacing every uppercase letter
# with the same lowercase letter.
# 
# 
# Example 1:
# 
# 
# Input: s = "Hello"
# Output: "hello"
# 
# 
# Example 2:
# 
# 
# Input: s = "here"
# Output: "here"
# 
# 
# Example 3:
# 
# 
# Input: s = "LOVELY"
# Output: "lovely"
# 
# 
# 
# Constraints:
# 
# 
# 1 <= s.length <= 100
# s consists of printable ASCII characters.
# 
# 
#

# @lc code=start
class Solution:
    def toLowerCase(self, s: str) -> str:
        return s.lower()
# @lc code=end

