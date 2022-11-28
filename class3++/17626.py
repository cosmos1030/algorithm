n = int(input())

set1 = set([i**2 for i in range(1, 224)])
# print(len(set1))
set2 = set()
for i in set1:
    for j in set1:
        sum = i+j
        if sum <= 50000:
            set2.add(sum)
# print(len(set2))
set3 = set()
for i in set1:
    for j in set2:
        sum = i+j
        if sum <= 50000:
            set3.add(sum)
# print(len(set3))

if n in set1:
    print(1)
elif n in set2:
    print(2)
elif n in set3:
    print(3)
else:
    print(4)
