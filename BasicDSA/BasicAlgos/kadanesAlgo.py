def maxSubArraySum(arr):
    n = len(arr)
    max_sum, curr_sum = arr[0], arr[0]
    for i in range(1, n):
        if curr_sum < 0:
            curr_sum = 0
        curr_sum += arr[i]
        max_sum = max(max_sum, curr_sum)
    
    return max_sum




if __name__ == "__main__":
    arr = [-2,1,-3,4,-1,2,1,-5,4]
    ans = maxSubArraySum(arr)
    print(ans)
