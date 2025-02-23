from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        num_map = {}  # Dictionary to store numbers and their indices
        
        for i, num in enumerate(nums):
            complement = target - num  # Find the required pair
            
            if complement in num_map:  # Check if complement exists in the map
                return [num_map[complement], i]  # Return indices of the pair
            
            num_map[num] = i  # Store the number with its index
        
        return []  # Edge case: If no solution found (shouldn't happen as per problem constraints)