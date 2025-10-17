
# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         letters = list(s)

#         l = 0
#         r = 1

#         length = 0

#         while r < len(letters):

#             if letters[r-1] != letters[r] and letters[l] == letters[r]:

#                 l += 1 
#                 r +=1

#                 if r < len(letters) and letters[l] == letters[r]:
#                     length +=1

#             else:
#                 length = 0
#                 r += 1
        
#         if length > 0:
#             return length
#         else:
#             return 1


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        letters = list(s)

        if len(letters) == 0:
            return 0

        l = 0
        r = 0

        frequency = {}

        count = 0

        while r < len(letters):

            print(f" $$$ Current letter is {letters[r]}")
            print(f"Have seen these letters so far {frequency}\n")

            

            if letters[r] in frequency:
                l = max(l, frequency[letters[r]] + 1)

                frequency[letters[r]] = r

            else:
                frequency[letters[r]] = r

            if (r - l + 1) > count:
                count = r - l + 1


            r += 1

        return count
            
    

sol = Solution()
# s="aab"
# s="zxyzxyz"
s = "dvdf"

print(sol.lengthOfLongestSubstring(s))