import sys
from collections import deque
input = sys.stdin.readline

def MakeLength4(n):
    t = 4-len(n)
    temp = ""
    for i in range(t):
        temp += "0"
    temp += n
    return temp

def D(n):
    n = str(int(n)*2%10000)
    n = MakeLength4(n)
    return n

def S(n):
    if n=='0000':
        n = str(9999)
    else:
        n = str(int(n)-1)
        n = MakeLength4(n)
    return n

def L(n):
    d1 = n[0]
    d2 = n[1]
    d3 = n[2]
    d4 = n[3]
    return d2+d3+d4+d1

def R(n):
    d1 = n[0]
    d2 = n[1]
    d3 = n[2]
    d4 = n[3]
    return d4+d1+d2+d3

t = int(input())
for _ in range(t):
    a, b = input().strip().split()
    a = MakeLength4(a)
    queue = deque([[a, ""]])
    visited = [False for i in range(10000)]
    while queue:
        temp = queue.popleft()
        # print(temp)
        if int(temp[0]) == int(b):
            print(temp[1])
            break
        if visited[int(D(temp[0]))] == False:
            queue.append([D(temp[0]), temp[1]+"D"])
            visited[int(D(temp[0]))] = True
        if visited[int(S(temp[0]))] == False:
            queue.append([S(temp[0]), temp[1]+"S"])
            visited[int(S(temp[0]))] = True
        if visited[int(L(temp[0]))] == False:
            queue.append([L(temp[0]), temp[1]+"L"])
            visited[int(L(temp[0]))] = True
        if visited[int(R(temp[0]))] == False:
            queue.append([R(temp[0]), temp[1]+"R"])
            visited[int(R(temp[0]))] = True

