from typing import List


# O(n) space and time

# class Solution:
#     def twoSum(self, numbers: List[int], target: int) -> List[int]:
#         nums = {}

#         complement = 0

#         for n in range(len(numbers)):
            
#             complement = target - numbers[n]
            

#             if numbers[n] not in nums:
#                 nums[numbers[n]] = n


#             if complement in nums and complement !=numbers[n]:

#                 if n < nums[complement]:
#                     return [n+1, nums[complement]+1]
#                 else:
#                     return [nums[complement]+1, n+1]

# O(n) time and O(1) space
class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:

        leftPointer = 0
        rightPointer = (len(numbers)) -1

        while leftPointer < rightPointer:
            sum = (numbers[leftPointer] + numbers[rightPointer])

            if target == sum:
                return [leftPointer + 1, rightPointer + 1]

            if sum < target:
                leftPointer += 1

            else:
                rightPointer -= 1
        

                

numbers = [1,2,3,4]
target = 3