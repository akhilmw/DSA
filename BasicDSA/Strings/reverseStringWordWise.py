def reverseStringWordWise(string) :
    n = len(string)
    ans = ""
    i = 0
    while i < n:
        while i < n and string[i] == ' ':
            i += 1
        # add this check to break out when i >= n otherwise one extra space will come in the starting.
        if i >= n:
            break
        j = i + 1
        while j < n and string[j] != ' ':
            j += 1
        sub = string[i:j]
        if len(ans) == 0:
            ans = sub
        else:
            ans  = sub + " " + ans
        i = j + 1

    return ans




if __name__ == '__main__':
    string = "  My Name   is Akhil  "
    ans = reverseStringWordWise(string)
    print(ans)

