
class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        max_profit = 0
        best_price = prices[0]
        for i in prices[1:]:
            
            if i < best_price:
                best_price = i
            
            elif i > best_price and ((i - best_price) > max_profit):
                    max_profit = i - best_price

        return max_profit
        
    
print(Solution().maxProfit([7,1,5,3,6,4]))


### this one exceed limit time which O(n2)
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         li = len(prices)
#         if li == 1:
#             return 0
#         elif li == 2 and (prices[1] <= prices[0]):
#             return 0
#         a= 0
#         for i in range(li): # 012
#             for j in range(li-1-i): # 0 
#                 b = prices[li-1-i] -prices[li-2-j-i] # last one

#                 if b > a:
#                     a = b
#         return a
