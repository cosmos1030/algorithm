n = int(input())
mylist = list(map(int, input().split()))
increase = [1 for _ in range(n)]
decrease = [1 for _ in range(n)]

for i in range(n):
    for j in range(i):
        if mylist[i] > mylist[j] and increase[i] <= increase[j]:
            increase[i] = increase[j] + 1

for i in range(n-1, -1, -1):
    for j in range(n-1, i, -1):
        if mylist[i] > mylist[j] and decrease[i] <= decrease[j]:
            decrease[i] = decrease[j] + 1
# print(increase)
# print(decrease)
max = 0
for i in range(n):
    if increase[i] + decrease[i]-1 > max:
        max = increase[i] + decrease[i] - 1

print(max)