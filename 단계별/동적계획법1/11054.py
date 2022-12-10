n = int(input())
mylist = list(map(int, input().split()))
length = [1 for i in range(n)]
increasing = [True for i in range(n)]

for i in range(n):
    