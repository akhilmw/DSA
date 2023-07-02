def firstMissingPositive(nums):
    n = len(nums)
    i = 0
    while i < n:
        correctPosn = nums[i] - 1
        while(nums[i] >=1 and nums[i] <= n and nums[i] != nums[correctPosn]):
            nums[i], nums[correctPosn] = nums[correctPosn], nums[i]
            correctPosn = nums[i] - 1
        i += 1 
    for i in range(n):
        if nums[i] != i + 1:
            return i+1
    
    return n + 1
    

if __name__ == '__main__':
    nums = [3, 4, 7, 1]
    print(firstMissingPositive(nums))