def equilibriumIndex(nums):
    totalSum = 0
    for x in nums:
        totalSum += x
    currSum = 0
    for i in range(len(nums)):
        totalSum -= nums[i]
        if currSum == totalSum:
            return i
        currSum += nums[i]
    
    return -1


if __name__ == '__main__':
    nums = [1,7,3,6,5,6]
    print(equilibriumIndex(nums))