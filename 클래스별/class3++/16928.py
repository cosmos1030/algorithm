import sys
from collections import deque

input = sys.stdin.readline

game = [0 for i in range(101)]

n, m = map(int, input().rstrip().split())
for i in range(n):
    x, y = map(int, input().rstrip().split())
    game[x] = y

for j in range(m):
    u,v = map(int, input().rstrip().split())
    game[u] = v

queue = deque([1])
visited = [False for _ in range(101)]
visited[1] = True
count_list = [0 for _ in range(101)]
count = 0

while queue:
    temp = queue.popleft()
    if temp == 100:
        break
    for element in [temp+1, temp+2, temp+3, temp+4, temp+5, temp+6]:
        if element>100:
            continue
        if visited[element] == False:
            visited[element] = True
            count_list[element] = count_list[temp] + 1
            if game[element]!=0:
                moved = game[element]
                if visited[moved] == True and count_list[element] > count_list[moved]:
                    continue
                else:
                    count_list[moved] = count_list[element]
                    visited[moved] = True
                    queue.append(moved)
            else:
                queue.append(element)
print(count_list[100])