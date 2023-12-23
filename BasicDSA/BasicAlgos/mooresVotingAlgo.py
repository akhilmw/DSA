def majorityElement(arr):
    n = len(arr)
    ele, count = 0, 0
    for i in range(0, n):
        if count == 0:
            ele = arr[i]
        if arr[i] == ele:
            count += 1
        else:
            count -= 1
    
    majority = 0
    for i in range(0, n):
        if arr[i] == ele:
            majority += 1
    
    if majority > n // 2:
        return ele
    
    return -1


if __name__ == "__main__":
    arr = [2,2,1,1,1,2,2]
    print(majorityElement(arr))
