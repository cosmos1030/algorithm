# 딕셔너리 자료형에 익숙해지기!

n = int(input())
cards = list(map(int, input().split()))
m = int(input())
numbers = list(map(int, input().split()))

mydic = dict.fromkeys(cards, 0)
# print(mydic)
for i in cards:
    mydic[i] += 1
# print(mydic)
for i in numbers:
    if i in mydic:
        print(mydic[i], end=" ")
    else:
        print(0, end=" ")