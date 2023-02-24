import sys
from collections import deque
input = sys.stdin.readline

n = int(input())
max_a, max_b, max_c = 0, 0, 0
min_a, min_b, min_c = 0, 0, 0
for i in range(n):
    a,b,c = map(int, input().split())
    a1 = a+ max_a
    b1 = b+max_b
    c1= c+max_c
    max_a = max(a1,b1)
    max_b = max(a1,b1,c1)
    max_c = max(b1,c1)
    a2=a+ min_a
    b2=b+ min_b
    c2=c+ min_c
    min_a = min(a2,b2)
    min_b = min(a2,b2,c2)
    min_c = min(b2,c2)
print(max(max_a,max_b, max_c), min(min_a, min_b, min_c))
