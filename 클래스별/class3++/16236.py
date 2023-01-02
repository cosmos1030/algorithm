import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
mylist = []
for i in range(n):
    mylist.append(list(map(int, input().strip().split())))

dx = [-1,0,0,1]
dy = [0,-1,1,0]
queue = deque()
size = 2
eat = 0
visited = [[False]*n for _ in range(n)]
time = 0

for i in range(n):
    for j in range(n):
        if mylist[i][j] == 9:
            queue.append([i,j,0])
            visited[i][j] = True
            mylist[i][j] = 0
            break
    if len(queue)!=0:
        break

while queue:
    # print(queue)
    temp_x, temp_y, count = queue.popleft()
    count += 1
    for i in range(4):
        x = temp_x + dx[i]
        y = temp_y + dy[i]
        if 0<=x<n and 0<=y<n and visited[x][y] == False:
            if mylist[x][y] != 0:
                if mylist[x][y] < size:
                    mylist[x][y] = 0
                    eat += 1
                    if eat==size:
                        size += 1
                        eat = 0
                    time += count
                    print(x, y, count)
                    # print(count)
                    count = 0
                    queue = deque([[x,y, count]])
                    visited = [[False]*n for _ in range(n)]
                    visited[x][y] = True
                    
                    break
                elif mylist[x][y] == size:
                    queue.append([x,y, count])
                    visited[x][y] = True
            else:
                queue.append([x,y, count])
                visited[x][y] = True
print(time)


