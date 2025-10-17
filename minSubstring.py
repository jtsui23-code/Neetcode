class Solution:
    def minWindow(self, s: str, t: str) -> str:

        if len(t) > len(s):
            return ""

        frequencyT = {}
        frequencyS = {}

        need = 0
        have = 0

        answers = {}

        l = 0

        for c in t:
            frequencyT[c] = 1 + frequencyT.get(c, 0)

        need = len(frequencyT)


        for r in range(len(s)):

            c = s[r]
            frequencyS[c] = 1 + frequencyS.get(c,0)

            if c in frequencyT:

                if frequencyS[c] == frequencyT[c]:
                    have += 1
                    print(f"have: {have}, need: {need}")

                
                
            while have == need:
                substr = s[l:r+1]
                answers[substr] = len(substr)
                
                frequencyS[s[l]] -= 1

                if s[l] in frequencyT and frequencyS[s[l]] < frequencyT[s[l]]:
                    have -= 1
                l += 1

                    

        if answers:
            substr = min(answers, key=answers.get)
            return substr
        else:
            return ""
        

        

        
        

        