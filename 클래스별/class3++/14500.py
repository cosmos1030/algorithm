import sys
input = sys.stdin.readline

n, m = map(int, input().strip().split())

mylist = []
maximum = 0
for i in range(n):
    temp = list(map(int, input().strip().split()))
    mylist.append(temp)
    if maximum < max(temp):
        maximum = max(temp)

mydic = {}
for i in range(maximum, 0, -1):
    mydic[i] = []
    for j in range(n):
        for k in range(m):
            if mylist[j][k] == i:
                mydic[i].append([j, k])

print(mydic)

