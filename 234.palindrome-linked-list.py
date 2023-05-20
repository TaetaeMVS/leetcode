#
# @lc app=leetcode id=234 lang=python3
#
# [234] Palindrome Linked List
#
# https://leetcode.com/problems/palindrome-linked-list/description/
#
# algorithms
# Easy (50.34%)
# Likes:    13818
# Dislikes: 756
# Total Accepted:    1.4M
# Total Submissions: 2.9M
# Testcase Example:  '[1,2,2,1]'
#
# Given the head of a singly linked list, return true if it is a palindrome or
# false otherwise.
# 
# 
# Example 1:
# 
# 
# Input: head = [1,2,2,1]
# Output: true
# 
# 
# Example 2:
# 
# 
# Input: head = [1,2]
# Output: false
# 
# 
# 
# Constraints:
# 
# 
# The number of nodes in the list is in the range [1, 10^5].
# 0 <= Node.val <= 9
# 
# 
# 
# Follow up: Could you do it in O(n) time and O(1) space?
#

# @lc code=start
# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def reverse(self, head):
        prev = None
        while head:
            next_node = head.next
            head.next = prev
            prev = head
            head = next_node
        return prev
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        # 1. find the middle node
        # 2. reverse the second half
        # 3. compare the first half and the second half
        if not head or not head.next:
            return True
        slow = fast = head
        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next
        second_half = self.reverse(slow)
        while second_half:
            if head.val != second_half.val:
                return False
            head = head.next
            second_half = second_half.next
        return True         
# @lc code=end

