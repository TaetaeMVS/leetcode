#
# @lc app=leetcode id=22 lang=python3
#
# [22] Generate Parentheses
#
# https://leetcode.com/problems/generate-parentheses/description/
#
# algorithms
# Medium (72.62%)
# Likes:    18242
# Dislikes: 740
# Total Accepted:    1.4M
# Total Submissions: 2M
# Testcase Example:  '3'
#
# Given n pairs of parentheses, write a function to generate all combinations
# of well-formed parentheses.
# 
# 
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
# Example 2:
# Input: n = 1
# Output: ["()"]
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 8
# 
# 
#

# @lc code=start
class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        def dfs(left, right, s):
            if len(s) == n * 2:
                res.append(s)
                return
            if left < n:
                dfs(left + 1, right, s + '(')
            if right < left:
                dfs(left, right + 1, s + ')')
        res = []
        dfs(0, 0, '')
        return res
        
# @lc code=end

