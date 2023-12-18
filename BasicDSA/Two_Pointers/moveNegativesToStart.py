def separateNegativeAndPositive(arr):
    i, j = 0, len(arr) - 1
    while i < j:
        if arr[i] > 0 and arr[j] < 0:
            arr[i], arr[j] = arr[j], arr[i]
            i += 1
            j -= 1
        elif arr[i] <= 0:
            i += 1
        else:
            j -= 1
    
    return arr

if __name__ == "__main__":
    arr = [1, 2, -3, 0, 4, -4, -5]
    print(separateNegativeAndPositive(arr))
