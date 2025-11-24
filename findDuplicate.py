from typing import List
class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        
        for num in nums:
            index = abs(num) - 1  # Use the number as an index (subtract 1 for 0-based indexing)
            
            if nums[index] < 0:  # If already negative, we found the duplicate
                return abs(num)
            
            nums[index] *= -1  # Mark as visited by making it negative