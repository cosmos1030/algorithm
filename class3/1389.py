from collections import deque

user_num, rel_num = map(int, input().split())
graph = [[] for i in range(user_num+1)]
for i in range(rel_num):
    user1, user2 = map(int, input().split())
    graph[user1].append(user2)
    graph[user2].append(user1)
INF = 1234567891
queue = deque()
min_num = INF
min_person = 0

for user in range(1, user_num+1):
    visited = []
    each_kevin_num = [0 for i in range(user_num+1)]
    queue.append(user)
    visited.append(user)
    while queue:
        temp = queue.popleft()
        # print(temp)
        for i in graph[temp]:
            if i not in visited:
                each_kevin_num[i] = each_kevin_num[temp]+1
                visited.append(i)
                queue.append(i)
    # print(each_kevin_num)
    if sum(each_kevin_num)<min_num:
        min_person = user
        min_num = sum(each_kevin_num)

print(min_person)