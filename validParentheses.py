
class Solution:
    def isValid(self, s: str) -> bool:
        
        front = {
            "[": "]",
            "{": "}",
            "(": ")"
        }

        back = {
            "]":"[",
            "}":"{",
            ")": "("
        }
        stack = []

        for i, c in enumerate(s):


            if c in back and len(stack) == 0:
                return False

            if c in front:
                stack.append(c)

            if c in back:
                
                bracket = stack[len(stack) - 1]

                if back[c] == bracket:
                    stack.pop()
                else:
                    return False

                if bracket not in front:
                    return False

        
        return len(stack) == 0

