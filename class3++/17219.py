import sys

n, m = map(int, input().split())

mydic = {}
for i in range(n):
    site, pw = sys.stdin.readline().strip().split()
    mydic[site] = pw
for i in range(m):
    site = sys.stdin.readline().strip()
    print(mydic[site])

