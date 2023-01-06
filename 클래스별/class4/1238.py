import sys
from collections import deque
input = sys.stdin.readline

n, m, x = map(int, input().split())
graph = [[] for i in range(n+1)]

for i in range(m):
    start, end, time = map(int, input().split())
    graph[start].append((end, time))

def bfs(start, end):
    queue = deque()
    queue.append(start)
    visited = [-1 for i in range(n+1)]
    visited[start] = 0
    while queue:
        temp = queue.popleft()
        for next, time in graph[temp]:
            if visited[next]==-1 or visited[next] > visited[temp] + time:
                visited[next] = visited[temp] + time
                queue.append(next)
    return visited[end]
times = []
for i in range(1, n+1):
    times.append(bfs(i, x)+bfs(x, i))

print(max(times))


