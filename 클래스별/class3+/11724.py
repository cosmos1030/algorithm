import sys
from collections import deque

n, m = map(int, sys.stdin.readline().strip().split())
graph = [[] for i in range(n+1)]
for i in range(m):
    u, v = map(int, sys.stdin.readline().strip().split())
    if v not in graph[u]:
        graph[u].append(v)
    if u not in graph[v]:
        graph[v].append(u)

queue = deque()
visited = set()
cnt = 0

for i in range(1, n+1):
    if i not in visited:
        queue = deque([i])
        while queue:
            temp = queue.popleft()
            for i in graph[temp]:
                if i not in visited:
                    queue.append(i)
                    visited.add(i)
        cnt += 1
print(cnt)