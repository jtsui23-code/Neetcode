class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        
        word1 = list(s)
        word2 = list(t)

        
        word1_count = {}
        word2_count = {}

        if len(word1) != len(word2):
            return False
        
        for i in range(len(word1)):


            if s[i] not in word1_count:
                
                word1_count[s[i]] = 1

            else:
                word1_count[s[i]] += 1

            if t[i] not in word2_count:

                word2_count[t[i]] = 1

            else:
                word2_count[t[i]] += 1


        if word1_count == word2_count:
            return True

        else:
            return False



            