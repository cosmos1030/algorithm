import sys, heapq
input = sys.stdin.readline
INF = 1234657891

n = int(input())
if n==1:
    print(0)
    sys.exit()
graph = [[] for i in range(n+1)]
for i in range(n-1):
    parent, child, weight = map(int, input().split())
    graph[parent].append((weight,child))
    graph[child].append((weight,parent))

def dijkstra(start):
    heap = []
    dp = [INF for i in range(n+1)]
    heapq.heappush(heap, (0, start))
    dp[start] = 0
    while heap:
        cur_wei, cur_pos = heapq.heappop(heap)
        for next_wei, next_pos in graph[cur_pos]:
            if dp[next_pos] > dp[cur_pos] + next_wei:
                dp[next_pos] = dp[cur_pos] + next_wei
                heapq.heappush(heap, (dp[next_pos], next_pos))
    max = 0
    max_index = 0
    for i in range(1, n+1):
        if dp[i] > max:
            max = dp[i]
            max_index = i
    return [max, max_index]
temp, temp_index = dijkstra(1)
result, result_index = dijkstra(temp_index)
print(result)