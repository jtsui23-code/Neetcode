from typing import List

# class Solution:
#     def maxProfit(self, prices: List[int]) -> int:
#         l = 0
#         r = len(prices) - 1

        
#         min = prices[l]
#         max = prices[r]

#         while l < r:
#             l += 1
#             r -= 1

#             print(f" $$$ Current Min is {min}")
#             print(f" $$$ Current Max is {max}")

#             if prices[l] < min:
#                 min = prices[l]
#                 print(f" $$$ New Min is {min}")


#             if prices[r] > max:
#                 max = prices[r]
#                 print(f" $$$ New Max is {max}")


#         if len(prices) == 2 and prices[len(prices) - 1] < prices[0]:
#             return 0
        
#         profit = (max - min)

#         if profit > 0:
#             return profit
        
#         else:
#             return 0


class Solution:
    def maxProfit(self, prices: List[int]) -> int:

        min = prices[0]

        profit = 0

        for p in prices:

            if (p - min) > 0 and (p - min) > profit:
                profit = (p - min)

            if p < min:
                min = p

        return profit
            

sol = Solution()
prices=[2,1,2,1,0,0,1]

print(sol.maxProfit(prices=prices))
