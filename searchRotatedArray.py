from typing import List

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        
        l = 0
        r = len(nums) - 1

        while l < r:

            m = (r+l) //2
            

            if target == nums[m]:
                return m

            elif nums[m] < nums[r]:
                if nums[m] < target <= nums[r]:
                    l = m + 1
                else:
                    r = m

            elif nums[m] > nums[r]:
                if nums[l] <= target < nums[m]:
                    r = m
                else:
                    l = m + 1
                

        if target == nums[l]:
            return l


        return -1