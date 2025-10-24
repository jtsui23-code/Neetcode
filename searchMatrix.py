from typing import List

class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        cols = len(matrix[0])

        left = 0
        right = rows * cols -1



        while left <= right:

            middle = (right + left)//2
            r = middle // cols
            c = middle % cols

            if target == matrix[r][c]:
                return True
            elif target > matrix[r][c]:
                left = middle + 1
            else:
                right = middle - 1

        return False


        
        