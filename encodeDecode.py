from typing import List

class Solution:


    def encode(self, strs: List[str]) -> str:
        encodedString = ""


        for s in strs:
            encodedString += f"{len(s)}#{s}"

        return encodedString

    def decode(self, s: str) -> List[str]:
        
        letters = list(s)
        letterNumbers = ""
        length = 0
        word = ""
        words = []
        readStr = False
        for letter in letters:

                  
            if length > 0 and readStr:
                word += letter
                length -= 1



            if not readStr and letter == '#':
                length = int(letterNumbers)

                if length == 0:
                    words.append("")
                    
                else:
                    word = ''
                    readStr = True

                    continue 

            elif not readStr:
                letterNumbers += letter

      

            if length <= 0 and readStr:

                letterNumbers = ''

                words.append(word)
                readStr = False

            

        return words



solution = Solution()
input = ["neet", "code", "love", "you"]

encodedStr = solution.encode(input)

print(f"Encoded message {encodedStr}")
decodedStr = solution.decode(encodedStr)

print(f"Decoded message {decodedStr}")