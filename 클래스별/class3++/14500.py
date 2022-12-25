import sys
input = sys.stdin.readline

N, M = map(int, input().strip().split())

mylist = []
for i in range(N):
    temp = list(map(int, input().strip().split()))
    mylist.append(temp)

visited = [[False]*M for _ in range(N)]
move = [(0,1),(0,-1),(1,0),(-1,0)]
maximum = 0

def dfs(i, j, dsum, cnt):
    global maximum
    if cnt == 4:
        maximum = max(maximum, dsum)
        return
    
    for n in range(4):
        ni = i+move[n][0]
        nj = j+move[n][1]
        if 0<=ni<N and 0<=nj<M and not visited[ni][nj]:
            visited[ni][nj] = True
            dfs(ni, nj, dsum + mylist[ni][nj], cnt+1)
            visited[ni][nj] = False

def exce(i, j):
    global maximum
    for n in range(4):
        tmp = mylist[i][j]
        for k in range(3):
            t = (n+k)%4
            ni = i+move[t][0]
            nj = j+move[t][1]

            if not (0<=ni<N and 0<=nj<M):
                tmp = 0
                break
            tmp += mylist[ni][nj]
        maximum = max(maximum,tmp)

for i in range(N):
    for j in range(M):
        visited[i][j] = True
        dfs(i,j, mylist[i][j],1)
        visited[i][j] = False
        exce(i, j)
print(maximum)