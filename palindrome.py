
class Solution:
    def isPalindrome(self, s: str) -> bool:
        word = list(s)

        length = len(word)

        leftPointer = 0
        rightPointer = length -1

        while leftPointer < rightPointer:

            while leftPointer < rightPointer and not word[leftPointer].isalnum():
                leftPointer += 1

            while leftPointer < rightPointer and not word[rightPointer].isalnum():
                rightPointer -=1

            
            if word[leftPointer].lower() != word[rightPointer].lower():
                return False
            
            leftPointer += 1
            rightPointer -=1

        return True

sol = Solution()
s="Was it a car or a cat I saw"

# s = "abb"
print(sol.isPalindrome(s))