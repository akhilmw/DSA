def pairSum(arr, target):
    count = 0
    i, j = 0, len(arr) - 1
    while i < j:
        sum = arr[i] + arr[j]
        if sum == target:
            count += 1
            i += 1
            j -= 1
        elif sum > 0:
            j -= 1
        else:
            i += 1
    
    if count == 0:
        return -1
    return count


if __name__ == "__main__":
    arr= [1, 2, 3, 4, 5, 6]
    ans = pairSum(arr, 7)
    print(ans)
