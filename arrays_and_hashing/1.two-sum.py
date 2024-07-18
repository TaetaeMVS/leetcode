class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        checked = {}
        for i in range(len(nums)):
            diff = target - nums[i]
            if diff in checked:
                return sorted([i, checked[diff]])
            checked[nums[i]] = i
