import sys

n, m = map(int, sys.stdin.readline().rstrip().split())
mylist1 = []
mylist2 = []

for i in range(n):
    temp = sys.stdin.readline().rstrip()
    mylist1.append(temp)

for i in range(m):
    temp = sys.stdin.readline().rstrip()
    mylist2.append(temp)

result = set(mylist1)&set(mylist2)
result = list(result)
result.sort()
print(len(result))
for i in result:
    print(i)