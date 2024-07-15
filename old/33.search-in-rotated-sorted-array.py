#
# @lc app=leetcode id=33 lang=python3
#
# [33] Search in Rotated Sorted Array
#
# https://leetcode.com/problems/search-in-rotated-sorted-array/description/
#
# algorithms
# Medium (40.25%)
# Likes:    25386
# Dislikes: 1507
# Total Accepted:    2.6M
# Total Submissions: 6.3M
# Testcase Example:  '[4,5,6,7,0,1,2]\n0'
#
# There is an integer array nums sorted in ascending order (with distinct
# values).
# 
# Prior to being passed to your function, nums is possibly rotated at an
# unknown pivot index k (1 <= k < nums.length) such that the resulting array is
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]]
# (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3
# and become [4,5,6,7,0,1,2].
# 
# Given the array nums after the possible rotation and an integer target,
# return the index of target if it is in nums, or -1 if it is not in nums.
# 
# You must write an algorithm with O(log n) runtime complexity.
# 
# 
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 5000
# -10^4 <= nums[i] <= 10^4
# All values of nums are unique.
# nums is an ascending array that is possibly rotated.
# -10^4 <= target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def search(self, nums: List[int], target: int) -> int:
        l, r = 0, len(nums) - 1
        while l <= r:
            mid = (l + r) // 2
            val = nums[mid]
            
            # base case
            if val == target:
                return mid
            
            # left sorted portion
            if val >= nums[l]:
                # left sorted portion, and target is larger than val
                # therefore target must be to the right of val
                if target > val:
                    l = mid + 1
                
                # left sorted portion and target is less than val
                else:
                    # if target is less than the left most value, and we are in the left sorted portion
                    # we need to check the right sorted portion
                    if target < nums[l]:
                        l = mid + 1
                    # target is greater than the left most value, and it is also greater than val
                    # we are in the left sorted portion, so we need to search to the right
                    else:
                        r = mid - 1
                        
                    
            # right sorted portion
            else:
                # right sorted portion, and target > val
                if target > val:
                    # right sorted portion, target > val and target is less than or equal to the right most value.
                    # therefore search to the right
                    if target <= nums[r]:
                        l = mid + 1
                
                    # right sorted portion, target > val, target is greater than the right most value
                    # therefore search to the left
                    else:
                        r = mid - 1
                    
                # right sorted portion, but target < val. 
                # therefore search left
                elif target < val:
                    r = mid - 1
                    
        return -1
                
            
# @lc code=end

