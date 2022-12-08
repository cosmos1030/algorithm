n = int(input())

cnt_dp = 0

def fibo_dp(n, dp):
    global cnt_dp
    for i in range(3,n+1):
        cnt_dp += 1
        dp.append(dp[i-1]+dp[i-2])
    return dp[n]

print(fibo_dp(n, [0,1,1]), cnt_dp)