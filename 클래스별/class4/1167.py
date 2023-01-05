import sys
from collections import deque

input = sys.stdin.readline

v = int(input())
graph = [[] for i in range(v+1)]

for i in range(v):
    templist = list(map(int, input().split()[:-1]))
    base = templist[0]
    for j in range(1, len(templist), 2):
        graph[base].append((templist[j], templist[j+1]))

def bfs(start):
    visit = [-1] * (v+1)
    queue = deque()
    queue.append(start)
    visit[start] = 0
    _max = [0,0] # 거리, edge

    while queue:
        t = queue.popleft()
        for edge, weight in graph[t]:
            if visit[edge] == -1:
                visit[edge] = visit[t] + weight
                queue.append(edge)
                if _max[0] < visit[edge]:
                    _max = visit[edge], edge
    return _max

distance, node = bfs(1)
distance, node = bfs(node)
print(distance)