def maxArea(arr):
    i, j = 0, len(arr) - 1
    res = 0
    while i < j:
        res = max(res, min(arr[i], arr[j])*(j - i))
        if arr[i] < arr[j]:
            i += 1
        else:
            j -= 1
    
    return res


if __name__ == "__main__":
    height = [1,8,6,2,5,4,8,3,7]
    res = maxArea(height)
    print(res)
