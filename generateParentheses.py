from typing import List

class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        open_par = 0
        close_par = 0
        
        current_str = ""
        result = []


        def backtrack(current_str, open_par, close_par):

            if open_par == n and close_par == n:
                result.append(current_str)
                current_str = ""

            elif open_par < n:
                
                backtrack(current_str + "(", open_par + 1, close_par)


            if close_par < n and close_par < open_par:
          

                backtrack(current_str + ")", open_par, close_par + 1)



        backtrack(current_str, open_par, close_par)

        return result

            

