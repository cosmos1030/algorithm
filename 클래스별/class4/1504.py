import sys
from collections import deque
input = sys.stdin.readline

n, e = map(int, input().split())
graph = [[] for i in range(n+1)]
for i in range(e):
    a, b, c = map(int, input().split())
    graph[a].append((b, c))
    graph[b].append((a, c))

v1, v2 = map(int, input().split())


def bfs(start, end):
    queue = deque()
    queue.append(start)
    visited = [-1 for i in range(n+1)]
    visited[start] = 0
    while queue:
        temp = queue.popleft()
        for edge, cost in graph[temp]:
            if visited[edge] == -1 or visited[edge] > visited[temp] + cost:
                visited[edge] = visited[temp] + cost
                queue.append(edge)
    return visited[end]
if bfs(1,v1) != -1 and bfs(v1,v2) != -1 and bfs(v2,n) != -1: 
    cand1 = bfs(1,v1)+bfs(v1,v2)+bfs(v2,n)
else:
    cand1 = 1234567891
if bfs(1,v2) != -1 and bfs(v2,v1) != -1 and bfs(v1,n) != -1: 
    cand2 = bfs(1,v2)+bfs(v2,v1)+bfs(v1,n)
else:
    cand2 = 1234567891
if min(cand1,cand2)==1234567891:
    print(-1)
else:
    print(min(cand1, cand2))