#
# @lc app=leetcode id=896 lang=python3
#
# [896] Monotonic Array
#
# https://leetcode.com/problems/monotonic-array/description/
#
# algorithms
# Easy (58.38%)
# Likes:    2018
# Dislikes: 63
# Total Accepted:    259.4K
# Total Submissions: 444.2K
# Testcase Example:  '[1,2,2,3]'
#
# An array is monotonic if it is either monotone increasing or monotone
# decreasing.
# 
# An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j].
# An array nums is monotone decreasing if for all i <= j, nums[i] >= nums[j].
# 
# Given an integer array nums, return true if the given array is monotonic, or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: nums = [1,2,2,3]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: nums = [6,5,4,4]
# Output: true
# 
# 
# Example 3:
# 
# 
# Input: nums = [1,3,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^5 <= nums[i] <= 10^5
# 
# 
#

# @lc code=start
class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        increasing = True
        decreasing = True
        for i in range(len(nums)-1):
            if nums[i] > nums[i+1]:
                decreasing = False
            if nums[i] < nums[i+1]:
                increasing = False
        if increasing or decreasing:
            return True
        else:
            return False
            
# @lc code=end

