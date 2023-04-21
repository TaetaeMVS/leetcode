#
# @lc app=leetcode id=1480 lang=python3
#
# [1480] Running Sum of 1d Array
#

# @lc code=start
class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        sum = 0
        for x in range(len(nums)):
            sum += nums[x]
            nums[x] = sum
        return nums
# @lc code=end

