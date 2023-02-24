import sys
from collections import deque

input = sys.stdin.readline

n,m= map(int, input().split())
graph = []
for i in range(n):
    temp = list(input().strip())
    for j in range(m):
        temp[j] = [temp[j], False]
    graph.append(temp)
# print(graph)

queue = deque()
queue.append([0,0])
graph[0][0] = [1, False]
dx= [0,0,1,-1]
dy = [1,-1,0,0]
while queue:
    tempx, tempy = queue.popleft()
    for i in range(4):
        movex, movey = tempx+dx[i], tempy+dy[i]
        if 0<=movex<n and 0<=movey<m:
            if graph[movex][movey][0] == '0':
                graph[movex][movey][0] = graph[tempx][tempy][0]+1
                graph[movex][movey][1] = graph[tempx][tempy][1]
                queue.append([movex, movey])
            if graph[movex][movey][0] == '1' and graph[tempx][tempy][1] == False:
                graph[movex][movey][0] = graph[tempx][tempy][0]+1
                graph[movex][movey][1] = True
                queue.append([movex, movey])
if graph[n-1][m-1][0] == '0':
    print(-1)
else:
    print(graph[n-1][m-1][0])