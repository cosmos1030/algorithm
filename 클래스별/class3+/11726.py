n = int(input())

dp = [1, 1]

for i in range(2,1001):
    dp.append(dp[i-2]+dp[i-1])

print(dp[n]%10007)