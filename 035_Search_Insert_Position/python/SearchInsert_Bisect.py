import bisect

class Solution:
    def searchInsert(self, nums: list[int], target: int) -> int:
        return bisect.bisect_left(nums, target)