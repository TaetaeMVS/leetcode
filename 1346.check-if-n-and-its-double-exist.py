#
# @lc app=leetcode id=1346 lang=python3
#
# [1346] Check If N and Its Double Exist
#

# @lc code=start
class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        for x in arr:
            if x * 2 in arr:
                if x == 0:
                    if arr.count(x) > 1:
                        return True
                else:
                    return True
        return False
        
# @lc code=end

