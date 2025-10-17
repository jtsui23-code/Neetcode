from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        
        operations = "-+*/"
        operands = [] 

        for c in tokens:

            if len(c) > 1:
                operands.append(int(c))

            elif c not in operations:
                operands.append(int(c))
                
            else:

                if c == "+":

                    temp = 0
                    op1 = operands.pop()
                    op2 = operands.pop()                    

                    temp = op1 + op2
                    operands.append(temp)

                elif c == "-":

                    temp = 0
                    op1 = operands.pop()
                    op2 = operands.pop()  

                    temp = op2 - op1

                    operands.append(temp)

                elif c == "*":

                    
                    temp = 0
                    op1 = operands.pop()
                    op2 = operands.pop()  

                    temp = op1 * op2

                    operands.append(temp)

                elif c == "/":
                    temp = 0
                    op1 = operands.pop()
                    op2 = operands.pop()  

                    temp = int(op2 / op1)

                    operands.append(temp)

        return operands[0]

               

            
