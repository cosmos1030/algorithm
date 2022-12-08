import sys
input = sys.stdin.readline

n = int(input())
mylist = list(map(int, input().strip().split()))

for i in range(1,n):
    if mylist[i]<mylist[i-1]+mylist[i]:
        mylist[i] += mylist[i-1]

print(max(mylist))