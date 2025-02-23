from typing import List

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        non_zeroes = [num for num in nums if num != 0]  # Collect non-zero elements
        zeroes_count = len(nums) - len(non_zeroes)  # Count of zeroes

        # Modify original list
        nums[:len(non_zeroes)] = non_zeroes
        nums[len(non_zeroes):] = [0] * zeroes_count
