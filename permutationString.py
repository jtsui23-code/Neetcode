
class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        
        if len(s1) > len(s2):
            return False

        l = 0

        frequencyS1 = {}
        frequencyS2 = {}

        for i in range(len(s1)):
            frequencyS1[s1[i]] = 1 + frequencyS1.get(s1[i], 0)

        for r in range(len(s2)):
            
            frequencyS2[s2[r]] = 1 + frequencyS2.get(s2[r], 0)

            if r - l >= len(s1):

                frequencyS2[s2[l]] -= 1
                if frequencyS2[s2[l]] == 0:
                    del frequencyS2[s2[l]]

                l += 1


            if frequencyS1 == frequencyS2:
                return True


        return False
