def rotateArray(nums, k) :

    def reverseList(arr, left, right):
        while left < right:
            arr[left], arr[right] = arr[right], arr[left]
            left += 1
            right -= 1

    n = len(nums)
    k = k % n
    reverseList(nums, 0, n-1)
    reverseList(nums, 0, k-1)
    reverseList(nums, k, n-1)

if __name__ == '__main__':

    nums = [1, 2, 3, 4, 5, 6, 7]
    rotateArray(nums, 3)
    print(nums)