def isSubsequence(str1, str2):
    n, m = len(str1), len(str2)
    i, j = 0, 0
    while i < n and j < m:
        if str1[i] == str2[j]:
            i += 1
        j += 1
    
    return i == n


if __name__ == "__main__":
    str1 = "abc"
    str2 = "ahbgdc"
    print(isSubsequence(str1, str2))