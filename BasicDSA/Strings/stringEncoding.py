def stringEncoding(message):
    ans = ""
    count = 0
    i = 0
    n = len(message)
    while i < n:
        j = i
        while j < n and message[j] == message[i]:
            count += 1
            j += 1
        if(len(ans) == 0):
            ans = message[i] + str(count)
        else:
            ans += message[i] + str(count)
        count = 0
        i = j
    
    return ans


if __name__ == "__main__":
    message = "aaaabbbccdaa"
    ans = stringEncoding(message)
    print(ans)
