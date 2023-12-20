# Find minimums and swap. -> basic rule for this algo

def min_index(arr, start, end):
    curr_min = float('inf')
    min_idx = -1
    for i in range(start, end):
        if arr[i] < curr_min:
            curr_min = arr[i]
            min_idx = i
    
    return min_idx


def selectionSort(arr):
    n = len(arr)
    for i in range(0, n-1):
        min_idx = min_index(arr, i, n)
        arr[i], arr[min_idx] = arr[min_idx], arr[i]
    
    return arr




if __name__ == "__main__":

    arr = [6, 5, 4, 3, 2, 1]
    print(selectionSort(arr))
