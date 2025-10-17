from typing import List

class Solution:
    
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        if len(position) < 1: 
            return 0

        sorted_pairs = sorted(zip(position, speed), reverse=True)

        ordered_pos, ordered_speed = zip(*sorted_pairs)

        time = [0] * len(ordered_pos)

        fleet = 1

        

        for p in range(len(ordered_pos)):
            time[p] = (target - ordered_pos[p])/ordered_speed[p]


        maxT = time[0]
        print(time)
        for t in range(1, len(time)):



            if time[t] > maxT:
                fleet += 1
            
                maxT = max(time[t], maxT)


        return fleet

            
           

        
