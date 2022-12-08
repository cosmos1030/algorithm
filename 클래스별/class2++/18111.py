import sys

n, m, b = map(int, sys.stdin.readline().rstrip().split())

mylist = []
for i in range(n):
    templist = list(map(int, sys.stdin.readline().rstrip().split()))
    mylist.append(templist)
# print(floors)
time = 500*500*256*2
height = 0

for floor in range(257):
    use_block = 0
    take_block = 0
    for j in mylist:
        for k in j:
            if floor>=k:
                use_block += floor-k
            else:
                take_block += k-floor
    left_block = take_block + b - use_block
    total_time = 2*take_block + use_block
    if left_block >= 0 and total_time <= time:
        time = total_time
        height = floor

print(time, height)