import sys
input = sys.stdin.readline

n = int(input())
mylist = list(map(int,input().strip().split()))
dp = [1 for i in range(n)]

for i in range(n):
    for j in range(i):
        if mylist[i] < mylist[j] and dp[i] <= dp[j]:
            dp[i] = dp[j] + 1

print(max(dp))