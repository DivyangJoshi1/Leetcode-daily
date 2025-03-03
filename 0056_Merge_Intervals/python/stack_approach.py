from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        # Step 1: Sort intervals based on start time
        intervals.sort(key=lambda x: x[0])
        
        stack = []
        
        # Step 2: Use stack to merge intervals
        for interval in intervals:
            if not stack or stack[-1][1] < interval[0]:
                stack.append(interval)
            else:
                stack[-1][1] = max(stack[-1][1], interval[1])
        
        return stack
