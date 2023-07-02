def findSecondLargest(arr):
    first_max = float('-inf')
    sec_max = float('-inf')
    for x in arr:
        if(x > first_max):
            sec_max = first_max
            first_max = x
        elif(x > sec_max and x != first_max):
            sec_max = x
    
    if(sec_max == float('-inf')):
        return -1
    
    return sec_max



if __name__ == '__main__':
    nums = [12, 35, 1, 10, 34, 1]
    print(findSecondLargest(nums))