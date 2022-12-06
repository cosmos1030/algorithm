import sys
input = sys.stdin.readline

channel_str = input()
channel = int(channel_str)
m = int(input())
if m == 0:
    broken = set()
else:
    broken = set(map(int, input().strip().split()))
closest = abs(channel-100)

for num in range(1000001):
    str_num = str(num)
    for j in range(len(str_num)):
        if int(str_num[j]) in broken:
            break
        if j == len(str_num)-1:
            closest = min(closest, abs(num-channel)+len(str_num))

print(closest)