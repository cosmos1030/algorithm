import sys
from collections import deque

input = sys.stdin.readline

n,m= map(int, input().split())
graph = []
for i in range(n):
    temp = list(input().strip())
    graph.append(temp)

dp = [[[0,0]]*m for i in range(n)]
dp[0][0] = [1, 0]

queue = deque()
queue.append([0,0])

dx = [0,0,1,-1]
dy = [1,-1,0,0]

while queue:
    tempx, tempy = queue.popleft()
    for i in range(4):
        x = tempx+dx[i]
        y = tempy+dy[i]
        if 0<=x<n and 0<=y<m:
            if graph[x][y] == '0':
                if dp[tempx][tempy][0] != 0:
                    dp[x][y][0] = dp[tempx][tempy][0]+1
                if dp[tempx][tempy][1] != 0:
                    dp[x][y][1] = dp[tempx][tempy][1]+1
                queue.append([x,y])
                graph[x][y] = -1
            if graph[x][y] == '1' and dp[tempx][tempy][1] == 0:
                dp[x][y][0] = 0
                dp[x][y][1] = dp[tempx][tempy][0] + 1
                queue.append([x,y])
                graph[x][y] = -1
print(dp)
if dp[n-1][m-1][0] == 0 and dp[n-1][m-1][1] == 0:
    print(-1)
elif dp[n-1][m-1][0] == 0:
    print(dp[n-1][m-1][1])
elif dp[n-1][m-1][1] == 0:
    print(dp[n-1][m-1][0])
else:
    print(min(dp[n-1][m-1][0], dp[n-1][m-1][1]))