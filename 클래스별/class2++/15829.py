# print(ord('b')-96)
length = int(input())
string = input()

sum = 0
for i in enumerate(string):
    sum += (ord(i[1])-96)*31**i[0]
print(sum%1234567891)