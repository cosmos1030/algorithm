import sys
input = sys.stdin.readline

n = int(input())
num = 1000000007

dp = [0, 1]

for i in range(2, n+1):
    dp.append(dp[i-1]%num+ dp[i-2]%num)

print(dp[n]%num)