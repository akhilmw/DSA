# Place the ele as its correct position

def insertionSort(arr):
    n = len(arr)
    for i in range(0, n):
        j = i
        while j > 0 and arr[j-1] > arr[j]:
            arr[j-1], arr[j] = arr[j], arr[j-1]
            j -= 1
    
    return arr

if __name__ == "__main__":
    arr = [6, 5, 4, 3, 2, 1]
    print(insertionSort(arr))
