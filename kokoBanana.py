from typing import List

class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        r = max(piles)

        l = 1

        ans = 0

        while l <= r:

            speed = (r+l) //2
            temp_hours = 0

            for b in piles:
                
                if b % speed != 0:
                    temp_hours += b//speed + 1
                else:
                    temp_hours += b//speed

                
            if temp_hours <= h:
                ans = speed
                r = speed - 1
            else:
                l = speed + 1

                

        return ans
            