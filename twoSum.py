from typing import List

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:

        numbers = {}

        for i, num in enumerate(nums):  
            
            print(f"The value of i is {i} and the value of num is {num}")
            complement = target - num

            print(f"Complement is {complement}")

            if complement in numbers:

                return [numbers[complement], i]
            
            numbers[num] = i



solution = Solution()
print(solution.twoSum([2,7, 11,9], 9))


