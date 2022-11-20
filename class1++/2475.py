mylist = list(map(int, input().split()))
sum = 0
for i in mylist:
    sum += i**2
print(sum%10)