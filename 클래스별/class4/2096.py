import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = []
for i in range(n):
    templist = list(map(int, input().split()))
    graph.append(templist)
# print(graph)

dp1 = [[0]*n for i in range(n)]
dp1[0] = graph[0]

for i in range(1, n):
    for j in range(0, n):
        if 0<=j-1<n:
            if 0<=j+1<n: 
                dp1[i][j] = max(dp1[i-1][j-1], dp1[i-1][j], dp1[i-1][j+1]) + graph[i][j]
            else:
                dp1[i][j] = max(dp1[i-1][j-1], dp1[i-1][j]) + graph[i][j]
        else:
            if 0<=j+1<n: 
                dp1[i][j] = max(dp1[i-1][j], dp1[i-1][j+1]) + graph[i][j]
            else:
                dp1[i][j] = dp1[i-1][j] + graph[i][j]

print(max(dp1[n-1]), end=" ")

dp2 = [[0]*n for i in range(n)]
dp2[0] = graph[0]

for i in range(1, n):
    for j in range(0, n):
        if 0<=j-1<n:
            if 0<=j+1<n: 
                dp2[i][j] = min(dp2[i-1][j-1], dp2[i-1][j], dp2[i-1][j+1]) + graph[i][j]
            else:
                dp2[i][j] = min(dp2[i-1][j-1], dp2[i-1][j]) + graph[i][j]
        else:
            if 0<=j+1<n: 
                dp2[i][j] = min(dp2[i-1][j], dp2[i-1][j+1]) + graph[i][j]
            else:
                dp2[i][j] = dp2[i-1][j] + graph[i][j]

print(min(dp2[n-1]))