# 덱을 이용한 빡구현
# 찾고자 하는 값에 표시를 해두어야 할때
# 이중리스트보단 리스트 2개를 이용하는게 편할지도??

from collections import deque

testcase = int(input())
for _ in range(testcase):
    n, m = map(int, input().split())
    mylist = list(map(int, input().split()))
    importances = deque()
    for importance in enumerate(mylist):
        # print(importance)
        importances.append(importance)
    count = 1
    while(1):
        if importances[0][1] < max(r[1] for r in importances):
            importances.append(importances.popleft())
        else:
            temp = importances.popleft()
            if temp[0] == m:
                print(count)
                break
            count += 1
            