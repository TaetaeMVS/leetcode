#
# @lc app=leetcode id=1716 lang=python3
#
# [1716] Calculate Money in Leetcode Bank
#
# https://leetcode.com/problems/calculate-money-in-leetcode-bank/description/
#
# algorithms
# Easy (66.13%)
# Likes:    569
# Dislikes: 16
# Total Accepted:    39.9K
# Total Submissions: 60.2K
# Testcase Example:  '4'
#
# Hercy wants to save money for his first car. He puts money in the Leetcode
# bank every day.
# 
# He starts by putting in $1 on Monday, the first day. Every day from Tuesday
# to Sunday, he will put in $1 more than the day before. On every subsequent
# Monday, he will put in $1 more than the previous Monday. 
# 
# Given n, return the total amount of money he will have in the Leetcode bank
# at the end of the n^th day.
# 
# 
# Example 1:
# 
# 
# Input: n = 4
# Output: 10
# Explanation: After the 4^th day, the total is 1 + 2 + 3 + 4 = 10.
# 
# 
# Example 2:
# 
# 
# Input: n = 10
# Output: 37
# Explanation: After the 10^th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) +
# (2 + 3 + 4) = 37. Notice that on the 2^nd Monday, Hercy only puts in $2.
# 
# 
# Example 3:
# 
# 
# Input: n = 20
# Output: 96
# Explanation: After the 20^th day, the total is (1 + 2 + 3 + 4 + 5 + 6 + 7) +
# (2 + 3 + 4 + 5 + 6 + 7 + 8) + (3 + 4 + 5 + 6 + 7 + 8) = 96.
# 
# 
# 
# Constraints:
# 
# 
# 1 <= n <= 1000
# 
# 
#

# @lc code=start
class Solution:
    def totalMoney(self, n: int) -> int:
        daily = 1
        sum = 0
        for i in range(n):
            sum += daily
            if i % 7 == 6:
                daily -= 5
            else:
                daily += 1
        return sum
# @lc code=end

