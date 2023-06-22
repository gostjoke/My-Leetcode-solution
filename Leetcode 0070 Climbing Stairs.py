'''
06/22/2023
n = 5
dp = [1, 1, 0, 0, 0, 0]

dp[2]：
dp = [1, 1, 2, 0, 0, 0]

dp[3]：
dp = [1, 1, 2, 3, 0, 0]

dp[4]：
dp = [1, 1, 2, 3, 5, 0]

dp[5]：
dp = [1, 1, 2, 3, 5, 8]
'''

one, two = 1,1
for i in range(n-1):
    print(one, two)
    one, two = two, one + two
return two
