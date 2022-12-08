# 10 m+1 = 12 n + 11 = k = 12 (10p+q)+11
# k mod 10 = 1
# k mod 12 = 11

# CRT(Chinese Remaider Theorem)

import sys
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    m, n, x, y = map(int, input().strip().split())
    k = x
    while(1):
        if (k-y) % n == 0:
            print(k)
            break
        else:
            k += m
        if k>m*n:
            print(-1)
            break