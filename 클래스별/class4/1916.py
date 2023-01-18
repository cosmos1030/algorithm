import sys
import heapq
input = sys.stdin.readline
INF = 1234567891

N = int(input())
M = int(input())

graph = [[] for i in range(N+1)]

for i in range(M):
    start, end, cost = map(int, input().split())
    graph[start].append((cost, end))
for i in range(N+1):
    graph[i].sort()

start, end = map(int, input().split())

def dijkstra(start, end):
    dp = [INF for i in range(N+1)]
    heap = []
    heapq.heappush(heap, (0,start))
    dp[start] = 0
    while heap:
        cur_cost, cur_pos = heapq.heappop(heap)
        for next_cost, next_pos in graph[cur_pos]:
            if dp[next_pos] > dp[cur_pos] + next_cost:
                dp[next_pos] = dp[cur_pos] + next_cost
                heapq.heappush(heap, (dp[next_pos], next_pos))
    return dp[end]

print(dijkstra(start, end))
