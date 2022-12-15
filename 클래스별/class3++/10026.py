import sys
from collections import deque
input = sys.stdin.readline
n = int(input())
paint = []

for i in range(n):
    temp = input().rstrip()
    paint.append(temp)

dx = [0,0,1,-1]
dy = [1,-1,0,0]
visited = [[False for _ in range(n)] for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        queue = deque()
        if visited[i][j] == False:
            result += 1
            color = paint[i][j]
            queue.append([i,j])
            visited[i][j] = True
            while queue:
                temp = queue.popleft()
                for k in range(4):
                    x = temp[0] + dx[k]
                    y = temp[1] + dy[k]
                    if x >=0 and x<n and y >=0 and y<n and (visited[x][y]==False) and (paint[x][y]==color):
                        visited[x][y] = True
                        queue.append([x,y])
print(result)

visited = [[False for _ in range(n)] for _ in range(n)]
result = 0

for i in range(n):
    for j in range(n):
        queue = deque()
        if visited[i][j] == False:
            result += 1
            color = paint[i][j]
            queue.append([i,j])
            visited[i][j] = True
            while queue:
                temp = queue.popleft()
                for k in range(4):
                    x = temp[0] + dx[k]
                    y = temp[1] + dy[k]
                    if x >=0 and x<n and y >=0 and y<n and (visited[x][y]==False) and (paint[x][y]==color):
                        visited[x][y] = True
                        queue.append([x,y])
print(result)