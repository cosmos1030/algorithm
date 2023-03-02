import sys
import heapq
input = sys.stdin.readline
INF = 1234567891

n= int(input())
m = int(input())
graph = [[] for i in range(n+1)]
for i in range(m):
    start, end, cost = map(int, input().split())
    graph[start].append([cost, end])

# print(graph)
def dijkstra(start):
    dp = [INF]*(n+1)
    dp[start] = 0
    queue = []
    heapq.heappush(queue, [dp[start], start])
    while queue:
        cur_dis, cur_node = heapq.heappop(queue)
        if dp[cur_node] < cur_dis:
            continue
        for new_dis, new_node in graph[cur_node]:
            distance = cur_dis + new_dis
            if distance < dp[new_node]:
                dp[new_node] = distance
                heapq.heappush(queue, [distance, new_node])
    for i in range(1, n+1):
        if dp[i] == INF:
            dp[i] = 0
        print(dp[i], end=" ")
    print("")

for i in range(1, n+1):
    dijkstra(i)


