import sys
import heapq
input = sys.stdin.readline

n = int(input())
myheap = []

for i in range(n):
    temp = int(input().strip())
    if temp==0:
        if len(myheap)==0:
            print(0)
        else:
            print(heapq.heappop(myheap)[1])
    else:
        if temp>=0:
            heapq.heappush(myheap, (temp, temp))
        else:
            heapq.heappush(myheap, (-temp-0.5, temp))