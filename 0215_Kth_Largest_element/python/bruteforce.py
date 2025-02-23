class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        nums.sort(reverse=True)  # Sort in descending order
        return nums[k - 1]  # Return the kth largest element
