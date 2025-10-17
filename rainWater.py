from typing import List



class Solution:
    def trap(self, height: List[int]) -> int:

        l = 0
        r = len(height) - 1

        lMax = height[l]
        rMax = height[r]

        water = 0

        while l < r:
            
            if height[l] < height[r]:

                temp = l
                l += 1

                if height[l] > lMax:
                    lMax = height[l]

                h = lMax - height[l]
                
                if h > 0:


                    print(f" **** index was {temp} height is {h}")

                    water += h

            
            elif height[l] >= height[r]:

                temp = r
                r -= 1

                if height[r] > rMax:
                    rMax = height[r]

                h = rMax - height[r]

                if h > 0:


                    water += h

            
        return water


sol = Solution()
height=[0,1,0,2,1,0,1,3,2,1,2,1]

print(sol.trap(height=height))


            

