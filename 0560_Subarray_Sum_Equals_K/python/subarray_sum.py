from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        count = 0
        sum_map = {0: 1}
        total = 0

        for num in nums:
            total += num
            if total - k in sum_map:
                count += sum_map[total - k]
            sum_map[total] = sum_map.get(total, 0) + 1

        return count
