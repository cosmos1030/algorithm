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
not_visited = set([i for i in range(1, n+1)])
cnt = 0
next = 1

while 1:
    queue = deque([next])
    while queue:
        temp = queue.popleft()
        for i in graph[temp]:
            if i in not_visited:
                queue.append(i)
                not_visited.remove(i)
    cnt += 1
    if len(not_visited)==0:
        break
    else:
        next = not_visited.pop()

print(cnt)