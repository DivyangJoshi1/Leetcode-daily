class Solution:
    def rotate(self, nums: list[int], k: int) -> None:
        n = len(nums)
        k %= n
        count = 0  # To keep track of moved elements
        start = 0  

        while count < n:
            curr = start
            prev = nums[start]
            while True:
                next_idx = (curr + k) % n
                nums[next_idx], prev = prev, nums[next_idx]
                curr = next_idx
                count += 1

                if start == curr:  # Cycle completed
                    break
            start += 1
