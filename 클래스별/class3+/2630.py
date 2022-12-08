n = int(input())
mylist = []
white = 0
blue = 0

for i in range(n):
    templist = list(map(int, input().split()))
    mylist.append(templist)

def recur(n, square):
    global white
    global blue
    # print(n, white, blue)
    if all(0 not in l for l in square):
        blue += 1
        return
    elif all(1 not in l for l in square):
        white += 1
        return
    sq1 = []
    sq2 = []
    sq3 = []
    sq4 = []
    for i in range(n//2):
        templist = []
        for j in range(n//2):
            templist.append(square[i][j])
        sq1.append(templist)
        templist = []
        for j in range(n//2, n):
            templist.append(square[i][j])
        sq2.append(templist)
    for i in range(n//2, n):
        templist = []
        for j in range(n//2):
            templist.append(square[i][j])
        sq3.append(templist)
        templist = []
        for j in range(n//2, n):
            templist.append(square[i][j])
        sq4.append(templist)
    recur(n//2, sq1)
    recur(n//2, sq2)
    recur(n//2, sq3)
    recur(n//2, sq4)
    return
recur(n, mylist)
print(white)
print(blue)
