import sys
input = sys.stdin.readline

a,b,c = map(int, input().split())
mylist = []
cnt = 0
while 1:
    if b == 1:
        mylist.append(1)
        break
    if b%2 == 0:
        mylist.append(0)
    else:
        mylist.append(1)
    b = b//2

dp = [a for i in range(len(mylist))]
for i in range(1,len(mylist)):
    dp[i] = dp[i-1]**2%c
result = 1
for i in range(len(mylist)):
    if mylist[i] !=0:   
        result *= mylist[i]*dp[i]
    # print(result)
print(result % c)
# print(mylist)
# print(dp)