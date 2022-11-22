import sys

n, m = map(int, input().split())
mylist = []
name_to_num = {}
num_to_name = {}
for i in range(1, n+1):
    temp = sys.stdin.readline().strip()
    name_to_num[temp] = i
    num_to_name[i] = temp
for j in range(m):
    temp = sys.stdin.readline().strip()
    try:
        print(name_to_num[temp])
    except:
        print(num_to_name[int(temp)])