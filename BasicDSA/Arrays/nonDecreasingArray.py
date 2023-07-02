def checkPossibility(nums):
    isChanged = False
    for i in range(len(nums)-1):
        if(nums[i] <= nums[i+1]):
            continue
        if isChanged:
            return False
        if(i == 0 or nums[i+1] >= nums[i-1]):
            nums[i] = nums[i+1]
        else:
            nums[i+1] = nums[i]
        isChanged = True
    
    return True

if __name__ == '__main__':
    nums = [1, 4, 1, 2]
    print(checkPossibility(nums))