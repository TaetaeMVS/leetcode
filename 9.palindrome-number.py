#
# @lc app=leetcode id=9 lang=python3
#
# [9] Palindrome Number
#

# @lc code=start
class Solution:
    def isPalindrome(self, x: int) -> bool:
        num_string = str(x)
        for i in range(len(num_string)):
            if num_string[i] != num_string[len(num_string) - i - 1]:
                return False
        return True
# @lc code=end

