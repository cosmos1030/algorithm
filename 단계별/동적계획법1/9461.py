import sys
input = sys.stdin.readline

dp = [0,1,1,1,2,2]
for i in range(6, 101):
    dp.append(dp[i-1]+dp[i-5])

for _ in range(int(input())):
    n = int(input())
    print(dp[n])

