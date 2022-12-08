n = int(input())

dp = [0 for i in range(n+1)]
dp[1] = 1
for i in range(2, n+1):
    min = 1234567891
    k = int(i**0.5)
    for j in range(1, k+1):
        if dp[i-j**2]<min:
            min = dp[i-j**2]
    dp[i] = (min+1)
print(dp[n])