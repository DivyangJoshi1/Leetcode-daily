from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        left = 0

        for right in range(len(nums)):
            if nums[right] != 0:
                if left != right:
                    nums[left], nums[right] = nums[right], nums[left]  # Swap only when needed
                left += 1
