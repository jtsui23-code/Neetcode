from typing import List

class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
             
        track = {}


        if len(nums) == 0:
            return 0

        
        answer = {}

        for n in nums:
            
            if n not in track:
                track[n] = 1

            
        for n in track:

            if n-1 not in track:
                answer[n] = 1

                count = n
                while count + 1 in track:
                    answer[n] += 1
                    count += 1
            
            

        return max(answer.values())

sol = Solution()

# nums = [2,20,4,10,3,4,5]
nums = [0,3,2,5,4,6,1,1]

print(sol.longestConsecutive(nums))
