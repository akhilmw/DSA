def longestSubsetWithZeroSum(arr):
    longest = 0
    myDict = {}
    sum = 0
    for i in range(len(arr)):
        sum += arr[i]
        if sum == 0:
            longest = i + 1
        else:
            if sum in myDict:
                longest = max(longest, i - myDict[sum])
            else:
                myDict[sum] = i
    
    return longest

if __name__ == "__main__":

    arr = [15, -2, 2, -8, 1, 7, 10, 23]
    ans = longestSubsetWithZeroSum(arr)
    print(ans)
    arr1 = [1 ,-1 ,2 ,-2 ]                  # example for sum == 0 then longest = i + 1
    ans1 = longestSubsetWithZeroSum(arr1)
    print(ans1)
