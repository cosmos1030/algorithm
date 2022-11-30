import sys
n = int(sys.stdin.readline())
mylist = [[] for i in range(n)]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    mylist[i] = temp
print(mylist[0:n//3][0:n//3])
mylist1 = []
mylist2 = []
mylist3 = []
for i in mylist[0:n//3]:
    mylist1.append(i[0:n//3])
    mylist2.append(i[n//3:n//3*2])
print(mylist1)