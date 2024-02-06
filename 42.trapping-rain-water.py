#
# @lc app=leetcode id=42 lang=python3
#
# [42] Trapping Rain Water
#
# https://leetcode.com/problems/trapping-rain-water/description/
#
# algorithms
# Hard (59.42%)
# Likes:    30478
# Dislikes: 459
# Total Accepted:    1.9M
# Total Submissions: 3.1M
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
from typing import List
class Solution:
    def trap(self, height: List[int]) -> int:
        water = [0 for x in height]
        l, r = 0, len(height) - 1
        maxL, maxR = height[l], height[r]
        while l < r:

            if maxL <= maxR:
                l += 1
                if height[l] > maxL:
                    maxL = height[l]
                current_water = maxL - height[l]
                if current_water > 0:
                    water[l] = current_water
            else:
                r -= 1
                if height[r] > maxR:
                    maxR = height[r]
                current_water = maxR - height[r]
                if current_water > 0:
                    water[r] = current_water
               
        return sum(water)
            

             
# @lc code=end

