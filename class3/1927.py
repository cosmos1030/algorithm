import sys
import heapq
n = int(input())
heap = []

for i in range(n):
    temp = int(sys.stdin.readline().strip())
    if temp==0:
        if len(heap)==0:
            print(0)
        else:
            result = heapq.heappop(heap)
            print(result)
    else:
        heapq.heappush(heap, temp)