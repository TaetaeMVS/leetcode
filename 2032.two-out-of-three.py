#
# @lc app=leetcode id=2032 lang=python3
#
# [2032] Two Out of Three
#
# https://leetcode.com/problems/two-out-of-three/description/
#
# algorithms
# Easy (73.64%)
# Likes:    606
# Dislikes: 35
# Total Accepted:    47.9K
# Total Submissions: 65K
# Testcase Example:  '[1,1,3,2]\n[2,3]\n[3]'
#
# Given three integer arrays nums1, nums2, and nums3, return a distinct array
# containing all the values that are present in at least two out of the three
# arrays. You may return the values in any order.
# 
# Example 1:
# 
# 
# Input: nums1 = [1,1,3,2], nums2 = [2,3], nums3 = [3]
# Output: [3,2]
# Explanation: The values that are present in at least two arrays are:
# - 3, in all three arrays.
# - 2, in nums1 and nums2.
# 
# 
# Example 2:
# 
# 
# Input: nums1 = [3,1], nums2 = [2,3], nums3 = [1,2]
# Output: [2,3,1]
# Explanation: The values that are present in at least two arrays are:
# - 2, in nums2 and nums3.
# - 3, in nums1 and nums2.
# - 1, in nums1 and nums3.
# 
# 
# Example 3:
# 
# 
# Input: nums1 = [1,2,2], nums2 = [4,3,3], nums3 = [5]
# Output: []
# Explanation: No value is present in at least two arrays.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= nums1.length, nums2.length, nums3.length <= 100
# 1 <= nums1[i], nums2[j], nums3[k] <= 100
# 
# 
#

# @lc code=start
class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        s1, s2, s3 = set(nums1), set(nums2), set(nums3)
        return list((s1 & s2) | (s1 & s3) | (s2 & s3)) 
# @lc code=end

