# 빡구현

import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input().strip()
pn = ''.join(['I' if i%2==0 else 'O' for i in range(2*n+1)])
# print(pn)
result  = 0

for i in range(m-2*n-1):
    # print(s[i: i+ 2*n+1])
    if s[i: i+ 2*n+1] == pn:
        result += 1
print(result)