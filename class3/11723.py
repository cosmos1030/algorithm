import sys

myset = set([])
m = int(sys.stdin.readline().strip())
for i in range(m):
    order = list(map(str, sys.stdin.readline().strip().split()))
    if len(order) == 1:
        a = order[0]
        if a == 'all':
            myset = set([i for i in range(1, 21)])
        else:
            myset.clear()
        continue
    else:
        a, b = order[0], order[1]
        b = int(b)
        if a == 'add':
            myset.add(b)
            continue
        elif a == 'check':
            print(1 if b in myset else 0)
        elif a == 'remove':
            myset.discard(b)
            continue
        else:
            if b in myset:
                myset.remove(b)
            else:
                myset.add(b)
