
from typing import List


class Solution:

    def hasDuplicate(self, nums: List[int]) -> bool:
        numbers = {}

        for num in nums:

            if num not in numbers:
                numbers[num] = 1

            elif num in numbers:
                numbers[num] += 1
                return True

        
        return False
            

solution = Solution()

print(solution.hasDuplicate([1,2, 3, 2]))






            
            

            

