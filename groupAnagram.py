from typing import List

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        
        # List of maps that count frequency of letters
        counters = [{}]
        group_anagram = {}

        tracker = 0
    
        for word in strs:
            
            letters = list(word)

            for letter in letters:

                if letter in counters[tracker]:

                    counters[tracker][letter] += 1

                else:
                    counters[tracker][letter] = 1
            
         
            if frozenset(counters[tracker].items()) in group_anagram:
                group_anagram[frozenset(counters[tracker].items())].append(word)
            
            else:
                group_anagram[frozenset(counters[tracker].items())] = [word]




            tracker += 1
            counters.append({})

            
        return list(group_anagram.values())

           



  
solution = Solution()

# strings = ["act","pots","tops","cat","stop","hat"]

strings = ["ddddddddddg","dgggggggggg"]
print(solution.groupAnagrams(strings))

            

    