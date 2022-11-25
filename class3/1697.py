n, k = map(int, input().split())
dp = [0 for i in range(max(n+1,k+1))]
for i in range(n):
    dp[i] = n-i
dp[n] = 0
for i in range(n+1, k+1):
    if i%2==0:
        dp[i] = min(dp[i//2], dp[i-1])+1
    else:
        dp[i] = min(dp[i-1], dp[(i+1)//2]+1)+1
print(dp[k])
