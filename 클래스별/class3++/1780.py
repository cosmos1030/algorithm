import sys
n = int(sys.stdin.readline())
mylist = [[] for i in range(n)]
for i in range(n):
    temp = list(map(int, sys.stdin.readline().split()))
    mylist[i] = temp
# print(mylist)
num_one = 0
num_zero = 0
num_minus_one = 0

def recur(mylist):
    # print(mylist)
    global num_one
    global num_zero
    global num_minus_one
    n = len(mylist)
    if all(0 not in l for l in mylist):
        if all(-1 not in l for l in mylist):
            num_one += 1
            return
        elif all(1 not in l for l in mylist):
            num_minus_one += 1
            return
    elif all(1 not in l for l in mylist):
        if all(-1 not in l for l in mylist):
            num_zero += 1
            return
    sublist1 = []
    sublist2 = []
    sublist3 = []
    sublist4 = []
    sublist5 = []
    sublist6 = []
    sublist7 = []
    sublist8 = []
    sublist9 = []
    for sublist in mylist[0:n//3]:
        sublist1.append(sublist[0:n//3])
        sublist2.append(sublist[n//3:n//3*2])
        sublist3.append(sublist[n//3*2:n])
    for sublist in mylist[n//3:n//3*2]:
        sublist4.append(sublist[0:n//3])
        sublist5.append(sublist[n//3:n//3*2])
        sublist6.append(sublist[n//3*2:n])
    for sublist in mylist[n//3*2:n]:
        sublist7.append(sublist[0:n//3])
        sublist8.append(sublist[n//3:n//3*2])
        sublist9.append(sublist[n//3*2:n])
    recur(sublist1)
    recur(sublist2)
    recur(sublist3)
    recur(sublist4)
    recur(sublist5)
    recur(sublist6)
    recur(sublist7)
    recur(sublist8)
    recur(sublist9)
recur(mylist)
print(num_minus_one)
print(num_zero)
print(num_one)