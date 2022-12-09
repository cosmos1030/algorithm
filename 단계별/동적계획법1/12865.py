import sys
input = sys.stdin.readline

num_stuff, max_weight = map(int, input().strip().split())

dp = [[0 for _ in range(max_weight+1)] for _ in range(num_stuff+1)]

stuff = [[0,0]]

for _ in range(num_stuff):
    stuff.append(list(map(int, input().strip().split())))

for i in range(num_stuff+1):
    weight = stuff[i][0]
    value = stuff[i][1]
    for j in range(max_weight+1):
        if j<weight:
            dp[i][j] = dp[i-1][j]
        else:
            dp[i][j] = max(dp[i-1][j], dp[i-1][j-weight]+value)

print(dp[num_stuff][max_weight])