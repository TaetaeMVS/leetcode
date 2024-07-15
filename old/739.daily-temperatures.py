#
# @lc app=leetcode id=739 lang=python3
#
# [739] Daily Temperatures
#
# https://leetcode.com/problems/daily-temperatures/description/
#
# algorithms
# Medium (65.92%)
# Likes:    12775
# Dislikes: 298
# Total Accepted:    888.9K
# Total Submissions: 1.3M
# Testcase Example:  '[73,74,75,71,69,72,76,73]'
#
# Given an array of integers temperatures represents the daily temperatures,
# return an array answer such that answer[i] is the number of days you have to
# wait after the i^th day to get a warmer temperature. If there is no future
# day for which this is possible, keep answer[i] == 0 instead.
# 
# 
# Example 1:
# Input: temperatures = [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]
# Example 2:
# Input: temperatures = [30,40,50,60]
# Output: [1,1,1,0]
# Example 3:
# Input: temperatures = [30,60,90]
# Output: [1,1,0]
# 
# 
# Constraints:
# 
# 
# 1 <= temperatures.length <= 10^5
# 30 <= temperatures[i] <= 100
# 
# 
#

# @lc code=start
from typing import List
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        answer = [0] * len(temperatures) 
        stack = []
        for i, temp in enumerate(temperatures):
            while stack and temp > stack[-1][0]:
                stackT, stackI = stack.pop()
                answer[stackI] = i - stackI
            stack.append([temp, i])
        return answer
    
s = Solution()
testCase = [73,74,75,71,69,72,76,73]
print(s.dailyTemperatures(testCase))
        # @lc code=end

