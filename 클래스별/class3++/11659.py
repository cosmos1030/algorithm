import sys
n, m = map(int, sys.stdin.readline().split())
numbers = list(map(int, sys.stdin.readline().split()))
sum = 0
sums = [0]
for i in numbers:
    sum += i
    sums.append(sum)

for _ in range(m):
    a, b = map(int, sys.stdin.readline().split())
    result = sums[b] - sums[a-1]
    print(result)