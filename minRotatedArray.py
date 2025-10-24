from typing import List

class Solution:
    def findMin(self, nums: List[int]) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:

            middle = (l+r)//2

            if nums[middle] < nums[r]:
                r = middle
            
            elif nums[middle] > nums[r]:
                l = middle +1


        return nums[l]