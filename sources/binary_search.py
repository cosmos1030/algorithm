def BinarySearch(arr, val, low, high):
    if low > high:
        return False #해당 배열에 타겟 숫자 미존재
    
    mid = (low + high) // 2 #위치 기반으로 찾는 것
    
    if arr[mid] > val:
        return BinarySearch(arr, val, low, mid - 1) #수가 중앙 값보다 아래 있는 경우
    elif arr[mid] < val:
        return BinarySearch(arr, val, mid + 1, high) #수가 중앙 값보다 위에 있는 경우
    else:
        return mid #아니면 숫자를 출력 -> return val

mylist = [2, 5, 7, 10, 15, 22]
print(BinarySearch(mylist, 22, 0, 5))