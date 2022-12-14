import sys
from collections import deque
input = sys.stdin.readline
m, n, h  = map(int, input().rstrip().split())
boxes = []
queue = deque()
for i in range(h):
    box = []
    for j in range(n):
        templist = list(map(int, input().rstrip().split()))
        for k in range(m):
            if templist[k] == 1:
                queue.append([i, j, k])
        box.append(templist)
    boxes.append(box)
# print(boxes)
dx = [0, 0, 0, 0, 1, -1]
dy = [0, 0, 1, -1, 0, 0]
dz = [1, -1, 0, 0, 0, 0]

# print(queue)

while queue:
    x, y, z = queue.popleft()
    for i in range(6):
        temp_x, temp_y, temp_z = x+dx[i], y+ dy[i], z+dz[i]
        if (temp_x < h and temp_x>=0) and (temp_y < n and temp_y >= 0) and (temp_z < m and temp_z >= 0):
            # print(temp_x, temp_y, temp_z)
            if boxes[temp_x][temp_y][temp_z]==0:
                boxes[temp_x][temp_y][temp_z] = boxes[x][y][z] + 1
                queue.append([temp_x, temp_y, temp_z])
# print(boxes)
max = 0
for i in boxes:
    for j in i:
        for k in j:
            if k >max:
                max = k
            if k == 0:
                print(-1)
                sys.exit()

print(max-1)


