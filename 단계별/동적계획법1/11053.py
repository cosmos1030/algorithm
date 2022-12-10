n = int(input())
mylist = list(map(int, input().split()))

length = [1 for i in range(n)]

for i in range(1, n):
    for j in range(i):
        if mylist[j]<mylist[i] and length[j]>= length[i]:
            length[i] = length[j] + 1

print(max(length))
