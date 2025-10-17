from typing import List

class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        
        days = []
        result = [0] * len(temperatures)

        for t in range(len(temperatures)):

            while days and temperatures[t] > temperatures[days[-1]]:

                result[days[-1]] = (t-days[-1])
                days.pop()
            
            days.append(t)

        return result
