# Push the max ele to the last --> basic idea

def bubbleSort(arr):
    n = len(arr)
    for i in range(n-1, -1, -1):
        for j in range(0, i):
            if arr[j+1] < arr[j]:
                arr[j+1], arr[j] = arr[j], arr[j+1]
    
    return arr

if __name__ == "__main__":

    arr = [6, 5, 4, 3, 2, 1]
    print(bubbleSort(arr))