from typing import List

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stack = []
        stack.append(heights[0])

        current = 1
        while stack and stack[-1] > heights[current]:
            pass
                        

