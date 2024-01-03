#
# @lc app=leetcode id=347 lang=python3
#
# [347] Top K Frequent Elements
#
# https://leetcode.com/problems/top-k-frequent-elements/description/
#
# algorithms
# Medium (62.77%)
# Likes:    16545
# Dislikes: 610
# Total Accepted:    1.9M
# Total Submissions: 3M
# Testcase Example:  '[1,1,1,2,2,3]\n2'
#
# Given an integer array nums and an integer k, return the k most frequent
# elements. You may return the answer in any order.
# 
# 
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
# 
# 
# Constraints:
# 
# 
# 1 <= nums.length <= 10^5
# -10^4 <= nums[i] <= 10^4
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
# 
# 
# 
# Follow up: Your algorithm's time complexity must be better than O(n log n),
# where n is the array's size.
# 
#

# @lc code=start
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        output = []
        for i in range(k):
            output.append(max(count, key=count.get))
            del count[max(count, key=count.get)]
        return output
        """
        
        """ My bucket sort
        counts_dict = {}
        for i in range(len(nums) + 1):
            counts_dict[i] = []
        count = {}
        for i in nums:
            if i not in count:
                count[i] = 1
            else:
                count[i] += 1
        output = [] 
        for key in count:
            counts_dict[count[key]].append(key)
        print(counts_dict)
        i = len(nums)
        output = []
        while i >= 0:
            if counts_dict[i] != []:
                for value in counts_dict[i]:
                    output.append(value)
            if len(output) == k:
                return output
            i -= 1
        """
        
        # Neetcode solution
        count = {}
        freq = [[] for x in range(len(nums) + 1)]
        
        for n in nums:
            count[n] = 1 + count.get(n, 0)
        for n, c in count.items():
            freq[c].append(n)
        
        res = []
        for i in range(len(freq) - 1, 0, -1):
            for n in freq[i]:
                res.append(n)
                if len(res) == k:
                    return res
            
                
            

        
# @lc code=end

