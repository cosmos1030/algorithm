import sys
input = sys.stdin.readline
N = int(input())
paper = [list(map(int, input().split())) for _ in range(N)]
num_minus = 0
num_zero = 0
num_plus = 0

def dfs(x, y, n):
    global num_minus, num_zero, num_plus
    num = paper[x][y]
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != paper[i][j]:
                for p in range(0,3):
                    for q in range(0,3):
                        dfs(x+n//3*p, y+n//3*q, n//3)
                return
    if num == 0:
        num_zero += 1
    elif num == 1:
        num_plus += 1
    else:
        num_minus += 1
    return
dfs(0,0,N)
print(num_minus)
print(num_zero)
print(num_plus)