import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    n = int(input())
    mylist1 = list(map(int, input().split()))
    mylist2 = list(map(int, input().split()))
    graph = [mylist1, mylist2]
    dp = [[0]*n for i in range(2)]
    dp[0][0] = graph[0][0]
    dp[1][0] = graph[1][0]
    if n==1:
        print(max(dp[0][0], dp[1][0]))
        continue
    else:
        dp[0][1] = dp[1][0] + graph[0][1]
        dp[1][1] = dp[0][0] + graph[1][1]
    for i in range(2, n):
        for j in range(2):
            if j==0:
                dp[j][i] = max(dp[j+1][i-1]+graph[j][i], dp[j+1][i-2]+graph[j][i])
            else:
                dp[j][i] = max(dp[j-1][i-1]+graph[j][i], dp[j-1][i-2]+graph[j][i])
    print(max(dp[0][n-1],dp[1][n-1]))