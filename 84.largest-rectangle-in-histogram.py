#
# @lc app=leetcode id=84 lang=python3
#
# [84] Largest Rectangle in Histogram
#
# https://leetcode.com/problems/largest-rectangle-in-histogram/description/
#
# algorithms
# Hard (42.84%)
# Likes:    14639
# Dislikes: 207
# Total Accepted:    685.1K
# Total Submissions: 1.6M
# Testcase Example:  '[2,1,5,6,2,3]'
#
# Given an array of integers heights representing the histogram's bar height
# where the width of each bar is 1, return the area of the largest rectangle in
# the histogram.
# 
# 
# Example 1:
# 
# 
# Input: heights = [2,1,5,6,2,3]
# Output: 10
# Explanation: The above is a histogram where width of each bar is 1.
# The largest rectangle is shown in the red area, which has an area = 10
# units.
# 
# 
# Example 2:
# 
# 
# Input: heights = [2,4]
# Output: 4
# 
# 
# 
# Constraints:
# 
# 
# 1 <= heights.length <= 10^5
# 0 <= heights[i] <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        max_area = 0
        stack = []
        heights.append(0)
        for i, h in enumerate(heights):
            if stack and h == stack[-1][1]:
                continue
            minStartindex = i
            while stack and h < stack[-1][1]:
                startIndex, height = stack.pop()
                minStartindex = startIndex
                max_area = max(max_area, height * (i - startIndex))
            stack.append((minStartindex, h))
        return max_area
# @lc code=end

