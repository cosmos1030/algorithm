# binary search

n, m = map(int, input().split())
trees = list(map(int, input().split()))

def binary_search(min, max, arr, target):
    mid = (min+max) // 2
    sum = 0
    for element in arr:
        if element>mid:
            sum += element - mid
    if sum>target:
        if mid+1>max:
            return mid
        return binary_search(mid+1, max, arr, target)
    elif sum<target:
        return binary_search(min, mid-1, arr, target)
    elif sum==target:
        return mid

print(binary_search(0, max(trees), trees, m))