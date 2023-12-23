# Approach 1
def sort012(arr):
    n = len(arr)
    c0, c1, c2 = 0, 0, 0
    for i in range(0, n):
        if arr[i] == 0:
            c0 += 1
        elif arr[i] == 1:
            c1 += 1
        else:
            c2 += 1
    
    i = 0
    while i < n and c0 > 0:
        arr[i] = 0
        i += 1
        c0 -= 1
    
    while i < n and c1 > 0:
        arr[i] = 1
        i += 1
        c1 -= 1
    
    while i < n and c2 > 0:
        arr[i] = 2
        i += 1
        c2 -= 1
    
    return arr


# Approach 2
# Basic Concept ->
# 1. Everything from 0 to low -1 will be 0
# 2. Everything from low to mid -1 will be 1
# 3. Everything from high +1 to n will be 2

def dutchNationalFlagAlgo(arr):
    n = len(arr)
    low, mid, high = 0, 0, n-1  
    while mid <= high:
        match arr[mid]:
            case 0:
                arr[low], arr[mid] = arr[mid], arr[low]
                low += 1
                mid += 1
            case 1:
                mid += 1
            case 2:
                arr[mid], arr[high] = arr[high], arr[mid]
                high -= 1
    
    return arr
        




if __name__ == "__main__":
    arr = [0, 1, 2, 1, 2, 1, 2]
    print(dutchNationalFlagAlgo(arr))
