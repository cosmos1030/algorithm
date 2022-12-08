n = input()
m = int(input())
if m==0:
    broken_buttons = []
else:
    broken_buttons = list(map(int, input().split()))
all_buttons = [i for i in range(10)]
remaining_buttons = list(set(all_buttons)-set(broken_buttons))

def getNearestBiggerNumber(num, arr):
    max = -10
    for element in arr:
        if num<element:
            if num-element>max:
                max = num-element
    if max == -10:
        return None
    else:
        return num-max

def getNearestSmallerNumber(num, arr):
    min = 10
    for element in arr:
        if num>element:
            if num-element<min:
                min = num-element
    if min == 10:
        return None
    else:
        return num-min

def checkSameNumber(num, arr):
    if num in arr:
        return True
    else:
        return False

# 더 큰 값 중 가장 가까운 값
result_num_larger = ""
for num in n:
    num = int(num)
    if checkSameNumber(num, remaining_buttons):
        result_num_larger += str(num)
        continue
    temp = getNearestBiggerNumber(num, remaining_buttons)
    if temp==None:
        result_num_larger = "123456789"
        break
    result_num_larger += str(temp)
    for _ in range(len(n)-len(result_num_larger)):
        result_num_larger += str(min(remaining_buttons))
    break
# print(result_num_larger)

# 더 작은 값 중 가장 가까운 값
result_num_smaller = ""
for num in n:
    num = int(num)
    if checkSameNumber(num, remaining_buttons):
        result_num_smaller += str(num)
        continue
    temp = getNearestSmallerNumber(num, remaining_buttons)
    if temp==None:
        result_num_smaller = "-123456789"
        break
    result_num_smaller += str(temp)
    for _ in range(len(n)-len(result_num_smaller)):
        result_num_smaller += str(max(remaining_buttons))
    break
# print(int(result_num_smaller))

# 가장 가까운 자릿수 작은 값
try:
    if len(n)>=2:
        result_num_smaller2 = ""
        for i in range(len(n)-1):
            result_num_smaller2 += str(max(remaining_buttons))
    else:
        result_num_smaller2 = "-123456789"
except:
    result_num_smaller2 = "-123456789"

# 가장 가까운 자릿수 큰 값
try:
    result_num_larger2 = ""
    for i in range(len(n)+1):
        if i ==0:
            result_num_larger2 += str(min(list(set(remaining_buttons)-set([0]))))
        else:
            result_num_larger2 += str(min(remaining_buttons))
except:
    result_num_larger2 = "123456789"
# print(result_num_larger2)

# if int(result_num_larger)>500000:
#     result_num_larger = "123456789"
# if int(result_num_larger2)>500000:
#     result_num_larger2 = "123456789"

print(result_num_larger, result_num_larger2, result_num_smaller, result_num_smaller2)

if int(n)<100:
    result = min(int(result_num_larger)-int(n)+len(str(int(result_num_larger))), int(n) - int(result_num_smaller)+len(str(int(result_num_smaller))), 100-int(n), int(n)-int(result_num_smaller2)+len(str(int(result_num_smaller2))), int(result_num_larger2)-int(n)+len(n)+1)
else:
    result = min(int(result_num_larger)-int(n)+len(str(int(result_num_larger))), int(n) - int(result_num_smaller)+len(str(int(result_num_smaller))), int(n)-100, int(n)- int(result_num_smaller2)+len(str(int(result_num_smaller2))), int(result_num_larger2)-int(n)+len(n)+1)

print(result)

# 47%

