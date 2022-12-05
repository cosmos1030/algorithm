import sys
input = sys.stdin.readline

str_n = input().strip()
n = int(str_n)
broken_num = int(input())
broken_buttons = set(map(int, input().strip().split()))
remaining_buttons = list(set([i for i in range(10)])-broken_buttons)
remaining_buttons.sort()

result1 = 0 # 단순히 +,-로 이동하는 경우
if n>=100:
    result1 += n-100
else:
    result1 += 100-n

result2 = len(str_n) # 같은 자릿수 중 크거나 같은 값을 입력하는 경우
SBN1 = "" # Smallest Bigger Number
for num in str_n:
    num = int(num)
    if num in remaining_buttons:
        SBN1 += str(num)
    else:
        for i in remaining_buttons:
            if i>num:
                SBN1 += str(i)
                print(len(str_n), len(SBN1))
                for j in range(len(str_n)-len(SBN1)):
                    SBN1 += str(min(remaining_buttons))
                break
        break
result2 += int(SBN1) - n
print(SBN1)

result3 = len(str_n) # 같은 자릿수 중 작거나 같은 값을 입력하는 경우
LSN1 = "" # Largest Smaller Number
for num in str_n:
    num = int(num)
    if num in remaining_buttons:
        LSN1 += str(num)
    else:
        for i in reversed(remaining_buttons):
            if i<num:
                LSN1 += str(i)
                print(len(LSN1))
                for j in range(len(str_n)-len(LSN1)):
                    LSN1 += str(max(remaining_buttons))
                break
        break
result3 += n - int(LSN1)
print(LSN1)

print(result1, result2, result3)