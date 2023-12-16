from collections import*

def groupAnagrams(listOfStr):
    res = defaultdict(list)
    for s in listOfStr:
        count = [0] * 26
        for c in s:
            count[ord(c) - ord("a")] += 1
        res[tuple(count)].append(s)
    
    return list(res.values())


if __name__ == "__main__":
    listOfStr = ["eat","tea","tan","ate","nat","bat"]
    ans = groupAnagrams(listOfStr)
    print(ans)