# 이중탐색! 같다고 해서 바로 종료시키지 말것!
# 함수에서 return 주의

k, n = map(int, input().split())
lancables = []
for i in range(k):
    lancables.append(int(input()))
# print(mylist)

def BinarySearch(arr, val, low, high):
    mid = (low+high)//2
    sum = 0
    for item in arr:
        sum += item//mid
    if sum<val:
        if low> mid-1:
            return mid-1
        return BinarySearch(arr, val, low, mid-1)
    elif sum>=val:
        if mid+1>high:
            return mid
        return BinarySearch(arr, val, mid+1, high) 

print(BinarySearch(lancables, n, 1, max(lancables)))

# 브루트포스

# for i in range(1, max(lancables)+1):
#     sum = 0
#     for lancable in lancables:
#         sum += lancable//i
#     if sum<n:
#         print(i-1)
#         break