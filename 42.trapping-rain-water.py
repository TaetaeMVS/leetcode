#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (59.32%)
# Likes:    26807
# Dislikes: 367
# Total Accepted:    1.5M
# Total Submissions: 2.6M
# Testcase Example:  '[0,1,0,2,1,0,1,3,2,1,2,1]'
#
# Given n non-negative integers representing an elevation map where the width
# of each bar is 1, compute how much water it can trap after raining.
# 
# 
# Example 1:
# 
# 
# Input: height = [0,1,0,2,1,0,1,3,2,1,2,1]
# Output: 6
# Explanation: The above elevation map (black section) is represented by array
# [0,1,0,2,1,0,1,3,2,1,2,1]. In this case, 6 units of rain water (blue section)
# are being trapped.
# 
# 
# Example 2:
# 
# 
# Input: height = [4,2,0,3,2,5]
# Output: 9
# 
# 
# 
# Constraints:
# 
# 
# n == height.length
# 1 <= n <= 2 * 10^4
# 0 <= height[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def trap(self, height: List[int]) -> int:
        first = 0
        last = len(height) - 1
        max_left = 0
        max_right = 0
        result = 0
        while first < last:
            if height[first] < height[last]:
                if height[first] >= max_left:
                    max_left = height[first]
                else:
                    result += max_left - height[first]
                first += 1
            else:
                if height[last] >= max_right:
                    max_right = height[last]
                else:
                    result += max_right - height[last]
                last -= 1
        return result
        
# @lc code=end

