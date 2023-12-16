def subArrayCount(arr, k):
    count = 0
    sum = 0
    rem = 0
    myDict = {rem : 1}
    for i in range(len(arr)):
        sum += arr[i]
        rem = sum % k
        if rem < 0:
            rem += k
        if rem in myDict:
            count += myDict[rem]
            myDict[rem] += 1
        else:
            myDict[rem] = 1
    
    return count

if __name__ == "__main__":
    arr = [5, 0, 2, 3, 1]
    ans = subArrayCount(arr, 5)
    print(ans)
