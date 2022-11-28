import sys

t = int(input())
for _ in range(t):
    temp = sys.stdin.readline().strip()
    stack = []
    vps = True
    for i in range(len(temp)):
        if temp[i] == '(':
            stack.append('(')
        else:
            if len(stack) != 0:
                stack.pop()
            else:
                vps = False
                break
    if len(stack)!= 0:
        vps = False
    if vps == False:
        print('NO')
    else:
        print('YES')