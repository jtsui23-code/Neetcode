from typing import List

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        
        answer = []
        frequency = {}
        
        for n, value in enumerate(nums):
            
            if value not in frequency:
                frequency[value] = 1

            elif value in frequency:
                frequency[value] += 1




        for i in range(k):
            
            bigValue = max(frequency, key=frequency.get())
            answer.append(bigValue)

            del frequency[bigValue]

        return answer
    
nums = [1,2,2,3,3,3]
# nums = [1,3,3,2,2,2]

solution = Solution()
print(solution.topKFrequent(nums, 2))






            