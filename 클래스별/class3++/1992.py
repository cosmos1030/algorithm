import sys
input = sys.stdin.readline

N = int(input())
mylist = [input().strip() for _ in range(N)]

def dfs(x, y, n):
    num = int(mylist[x][y])
    for i in range(x, x+n):
        for j in range(y, y+n):
            if num != int(mylist[i][j]):
                print('(', end="")
                dfs(x, y, n//2)
                dfs(x, y +n//2, n//2)
                dfs(x+n//2, y, n//2)
                dfs(x+n//2, y +n//2, n//2)
                print(')', end="")
                return
    if num == 0:
        print(0, end="")
    else:
        print(1, end="")
    return

dfs(0,0,N)
print("")