#
# @lc app=leetcode id=74 lang=python3
#
# [74] Search a 2D Matrix
#
# https://leetcode.com/problems/search-a-2d-matrix/description/
#
# algorithms
# Medium (49.54%)
# Likes:    15203
# Dislikes: 403
# Total Accepted:    1.6M
# Total Submissions: 3.3M
# Testcase Example:  '[[1,3,5,7],[10,11,16,20],[23,30,34,60]]\n3'
#
# You are given an m x n integer matrix matrix with the following two
# properties:
# 
# 
# Each row is sorted in non-decreasing order.
# The first integer of each row is greater than the last integer of the
# previous row.
# 
# 
# Given an integer target, return true if target is in matrix or false
# otherwise.
# 
# You must write a solution in O(log(m * n)) time complexity.
# 
# 
# Example 1:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 13
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# m == matrix.length
# n == matrix[i].length
# 1 <= m, n <= 100
# -10^4 <= matrix[i][j], target <= 10^4
# 
# 
#

# @lc code=start
class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        topR, bottomR = 0, len(matrix) - 1
        while topR <= bottomR:
            
            midR = (bottomR + topR) // 2
            # print("Searching row " + str(midR))
            if target > matrix[midR][-1]:
                """
                print("target > matrix[midR][-1], \
                      MidR = " + str(midR) + \
                          "matrix[midR][-1] = " + str(matrix[midR][-1]))
                """
                topR = midR + 1
            elif target < matrix[midR][0]:
                bottomR = midR - 1
                """
                print("target < matrix[midR][0]" + 
                      "\n matrix[midR][0] = " + str(matrix[midR][0]))
                print("Set bottomR to " + str(bottomR))
                """
            else:
                # execute binary search
                # print("Executing binary search")
                l, r = 0, len(matrix[midR]) - 1
                while l <= r:
                    i = (l + r) // 2
                    if matrix[midR][i] == target:
                        return True
                    elif matrix[midR][i] < target:
                        l = i + 1
                    else:
                        r = i - 1
                return False
        return False
# @lc code=end

