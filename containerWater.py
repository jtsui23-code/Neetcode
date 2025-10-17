from typing import List


class Solution:
    def maxArea(self, heights: List[int]) -> int:
        
        leftPointer = 0
        rightPointer = len(heights) - 1
        maxWater = 0
        
        while leftPointer < rightPointer:
            # Calculate current area
            width = rightPointer - leftPointer
            height = min(heights[leftPointer], heights[rightPointer])
            currentArea = width * height
            
            # Update max
            maxWater = max(maxWater, currentArea)
            
            # Move the pointer pointing to the shorter line
            if heights[leftPointer] < heights[rightPointer]:
                leftPointer += 1
            else:
                rightPointer -= 1

        return maxWater
            


