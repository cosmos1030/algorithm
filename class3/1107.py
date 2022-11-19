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
        result_num += str(num)
        # print(result_num)
        continue
    temp = getNearestBiggerNumber(num, remaining_buttons)
    # print(temp)
    result_num_larger += str(temp)
    for _ in range(len(n)-len(result_num_larger)):
        result_num_larger += str(min(remaining_buttons))
    break
print(result_num_larger)

# 더 작은 값 중 가장 가까운 값
result_num_smaller = ""
for num in n:
    num = int(num)
    if checkSameNumber(num, remaining_buttons):
        result_num += str(num)
        # print(result_num)
        continue
    temp = getNearestSmallerNumber(num, remaining_buttons)
    # print(temp)
    result_num_smaller += str(temp)
    for _ in range(len(n)-len(result_num_smaller)):
        result_num_smaller += str(max(remaining_buttons))
    break
print(result_num_smaller)