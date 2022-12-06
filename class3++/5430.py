import sys
from collections import deque
input = sys.stdin.readline

t = int(input())
for _ in range(t):
    order = input().strip()
    n = int(input().strip())
    temp = input().strip()
    left = True
    try:
        queue = deque(map(int, temp[1:-1].split(",")))
    except:
        queue = deque()
    checkerror = False
    for i in order:
        if i=='D':
            if len(queue)==0:
                checkerror = True
                break
            else:
                if left==True:
                    queue.popleft()
                else:
                    queue.pop()
        else:
            if left==True:
                left = False
            else:
                left = True
    if checkerror == True:
        print("error")
    else:
        print("[", end="")
        if left == True:
            while queue:
                if len(queue)==1:
                    print(str(queue.popleft()), end="")
                else:
                    print(str(queue.popleft())+",", end="")
        else:
            while queue:
                if len(queue)==1:
                    print(str(queue.pop()), end="")
                else:
                    print(str(queue.pop())+",", end="")
        print("]")
