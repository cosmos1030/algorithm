# 패턴

import sys
input = sys.stdin.readline

n = int(input())
len_s = int(input())
s = input().strip()

result = 0
count = 0
i = 0

while(i<=len_s-3):
    if s[i: i+3] == 'IOI':
        count += 1
        if count == n:
            result += 1
            count -= 1
        i += 2
    else:
        i += 1
        count = 0
print(result)