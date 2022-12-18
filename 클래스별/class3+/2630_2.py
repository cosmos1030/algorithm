import sys
input = sys.stdin.readline

n = int(input())
paper = []

for i in range(n):
    templist = list(map(int, input().strip().split()))
    paper.append(templist)

num_white = 0 # 0
num_blue = 0

def recur(paper, n):
    global num_white, num_blue
    color = paper[0][0]
    for i in range(n):
        for j in range(n):
            if paper[i][j] != color:
                paper1 = []
                paper2 = []
                paper3 = []
                paper4 = []
                for temp in paper[:n//2]:
                    paper1.append(temp[:n//2])
                    paper2.append(temp[n//2:])
                for temp in paper[n//2:]:
                    paper3.append(temp[:n//2])
                    paper4.append(temp[n//2:])
                recur(paper1, n//2)
                recur(paper2, n//2)
                recur(paper3, n//2)
                recur(paper4, n//2)
                return
    if color==0:
        num_white += 1
    else:
        num_blue += 1

recur(paper, n)
print(num_white)
print(num_blue)
