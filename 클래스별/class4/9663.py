n = int(input())

ans = 0
row = [0] * n # 한 줄에는 하나의 퀸만 올 수 있음
def ispossible(x):
    for i in range(x):
        if row[x] == row[i] or abs(row[x] - row[i]) == abs(x-i):
            return False
    return True

def n_queens(x):
    global ans
    if x==n: # 모든 줄에 퀸을 다 놓은 경우
        ans += 1
        return
    else:
        for i in range(n):
            row[x] = i
            if ispossible(x):
                n_queens(x+1) # 다음 줄에 퀸 놓기

n_queens(0)
print(ans)