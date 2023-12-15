# Approach 1 using sets
def minElementsToRemove1(arr):
    mySet = set()
    for i in range(len(arr)):
        mySet.add(arr[i])
    return len(arr) - len(mySet)

# Approach 2 using map/dict

def minElementsToRemove2(arr):
    count = 0
    myDict = {}
    for i in range(len(arr)):
        value = myDict.get(arr[i], 0)
        if value > 0:
            count += 1
        else:
            myDict[arr[i]] = 1
    return count


if __name__ == "__main__":
    arr = [2, 5, 3, 1, 3, 5]
    ans = minElementsToRemove1(arr)
    print(ans)
    ans1 = minElementsToRemove2(arr)
    print(ans1)