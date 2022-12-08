import sys
t = int(sys.stdin.readline())
for _ in range(t):
    n = int(sys.stdin.readline())
    mydic = {}
    for _ in range(n):
        name, type = sys.stdin.readline().strip().split()
        if type in mydic:
            mydic[type].add(name)
        else:
            mydic[type] = set([name])
    result = 1
    for key in mydic:
        result *= len(mydic[key])+1
    print(result-1)