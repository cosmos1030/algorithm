import sys
import heapq

t = int(sys.stdin.readline().strip())

for _ in range(t):
    k = int(sys.stdin.readline().strip())
    max_heap = []
    max_heap_removed = []
    min_heap = []
    min_heap_removed = []
    for i in range(k):
        if max_heap_removed and min_heap:
            while max_heap_removed[0] == min_heap[0]:
                heapq.heappop(max_heap_removed)
                heapq.heappop(min_heap)
                if not (max_heap_removed and min_heap):
                    break
        if min_heap_removed and max_heap:
            while min_heap_removed[0] == max_heap[0]:
                heapq.heappop(min_heap_removed)
                heapq.heappop(max_heap)
                if not (min_heap_removed and max_heap):
                    break

        order, num = sys.stdin.readline().strip().split()
        num = int(num)
        if order=='I':
            heapq.heappush(min_heap, num)
            heapq.heappush(max_heap, -num)
        else:
            if num==1: #최댓값 삭제
                if max_heap:
                    temp = -heapq.heappop(max_heap)
                    heapq.heappush(max_heap_removed, temp)
            else: #최솟값 삭제
                if min_heap:
                    temp = heapq.heappop(min_heap)
                    heapq.heappush(min_heap_removed, -temp)
    if max_heap_removed and min_heap:
        while max_heap_removed[0] == min_heap[0]:
            heapq.heappop(max_heap_removed)
            heapq.heappop(min_heap)
            if not (max_heap_removed and min_heap):
                break
    if min_heap_removed and max_heap:
        while min_heap_removed[0] == max_heap[0]:
            heapq.heappop(min_heap_removed)
            heapq.heappop(max_heap)
            if not (min_heap_removed and max_heap):
                break
    if len(min_heap) == len(max_heap_removed):
        print('EMPTY')
    else:
        print(-max_heap[0], min_heap[0])