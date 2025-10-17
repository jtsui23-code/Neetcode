from typing import List

class Solution:
    def maxSlidingWindow(self, nums: List[int], k: int) -> List[int]:
        answer = []
        temp = {}

        l = 0

        for r in range(len(nums)):
            temp[r] = nums[r]


            if (r - l + 1) > k:
                del temp[l]
                l += 1

            if (r - l + 1) == k:
                
                key = max(temp, key=temp.get)

                answer.append(temp[key])
                
            

        return answer
