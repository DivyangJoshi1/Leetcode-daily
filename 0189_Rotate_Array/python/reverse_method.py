class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n  # Handle cases where k > n

        def reverse(start, end):
            while start < end:
                nums[start], nums[end] = nums[end], nums[start]
                start += 1
                end -= 1

        reverse(0, n - 1)   # Reverse the whole array
        reverse(0, k - 1)   # Reverse the first k elements
        reverse(k, n - 1)   # Reverse the last n-k elements