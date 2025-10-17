from typing import List

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        answer = []
        nums.sort()

        for i in range(len(nums)):
            
            if nums[i] == nums[i-1] and i > 0:
                continue

            leftPointer = i + 1
            rightPointer = len(nums) - 1

            while leftPointer < rightPointer:
                
                if nums[i] + nums[leftPointer] + nums[rightPointer] == 0:


                    answer.append([nums[i], nums[leftPointer], nums[rightPointer]])

                    while leftPointer < rightPointer and nums[leftPointer] == nums[leftPointer+1]:
                        leftPointer += 1
                        
                    while leftPointer < rightPointer and nums[rightPointer] == nums[rightPointer-1]:

                        rightPointer -= 1

                    leftPointer += 1
                    rightPointer -= 1


                elif nums[i] + nums[leftPointer] + nums[rightPointer] > 0:
                    rightPointer -= 1

                elif nums[i] + nums[leftPointer] + nums[rightPointer] < 0:
                    leftPointer += 1

        return answer


                