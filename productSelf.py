from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        
        
        result = [1] * len(nums)

        prefix = 1

        for i in range(len(nums)):

            result[i] = prefix
            prefix *= nums[i]

        postPrefix = 1

        for i in reversed(range(len(nums))):
            result[i] *= postPrefix
            
            postPrefix *= nums[i]


        return result



            
solution = Solution()
