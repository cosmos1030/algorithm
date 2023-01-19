from collections import deque

middle = list(input())


def multi(queue):
    cnt = 0
    init = queue[0][0]
    while 1:
        now = queue.popleft()
        if now[0] == init:
            cnt += 1
        if cnt == 2:
            queue.appendleft(now)
            break
        if now == '*' or now=='/':
            next = queue.popleft()
            last = queue.pop()
            token = last+next+now
            # print(token)
            queue.append(token)
        else:
            queue.append(now)
    return queue

def add(queue):
    cnt = 0
    init = queue[0][0]
    while 1:
        now = queue.popleft()
        if now[0] == init:
            cnt += 1
        if cnt == 2:
            queue.appendleft(now)
            break
        if now == '+' or now=='-':
            next = queue.popleft()
            last = queue.pop()
            token = last+next+now
            # print(token)
            queue.append(token)
        else:
            queue.append(now)
    return queue

while '(' in middle:
    left = -1
    right = 1234567891
    for i in range(len(middle)):
        if middle[i] =='(':
            if left < i:
                left = i
    for i in range(len(middle)):
        if middle[i] == ')':
            if right > i and left<i:
                right = i
    # print(left, right)
    # print(middle[left+1:right])
    queue = deque(middle[left+1:right])
    # print(queue)
    queue = multi(queue)
    queue = add(queue)
    # print(queue)
    if right==len(middle)-1:
        middle = middle[:left]+list(queue)
    else:
        middle = middle[:left]+list(queue)+middle[right+1:]
    # print(middle)

queue = deque(middle)
queue = multi(queue)
queue = add(queue)

print(queue.pop())
