from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        maxArea = 0

        for i, h in enumerate(heights):
            
            while stack and stack[-1][1] > h:
                tall = stack[-1][1]
                stack.pop()

                width = 0

                if not stack: 
                    width = i
                else:
                    width = i - stack[-1][0] - 1

                area = width * tall

                maxArea = max(area, maxArea)
            
            stack.append((i,h))


        while stack:
            i, tall = stack.pop()
            
            width = 0
            if not stack:
                width = len(heights)

            else:
                width = len(heights) - stack[-1][0] - 1

            area = width * tall

            maxArea = max(maxArea, area)


        return maxArea

                        


                        

