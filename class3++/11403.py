import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n)]

for i in range(n):
    templist = list(map(int, input().strip().split()))
    for j in range(n):
        if templist[j]==1:
            graph[i].append(j)

for row in range(n):
    queue = deque([row])
    visited = [False for _ in range(n)]
    while queue:
        temp = queue.popleft()
        # print(temp)
        for i in graph[temp]:
            if visited[i] == False:
                queue.append(i)
                visited[i] = True

    for i in range(n):
        if visited[i]==True:
            print(1, end=" ")
        else:
            print(0, end=" ")
    print("")