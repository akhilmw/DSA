# This will generate a beautiful string of size n
def generate(n, zero):
    ans = ""
    if n == 0:
        return ans
    if zero:            # string should start with 0
        ans += '0'
        n -= 1
    else:               # string should start with 1
        ans += '1'
        n -= 1
    while n > 0:
        ans += '0' if ans[-1] == '1' else '1'
        n -= 1

    return ans

def difference(str, ans):
    count = 0
    for i in range(len(str)):
        if str[i] != ans[i]:
            count += 1
    return count


def makeBeautiful(str):
    n = len(str)
    ans1 = generate(n, True)
    diff1 = difference(str, ans1)
    ans2 = generate(n, False)
    diff2 = difference(str, ans2)

    return min(diff1, diff2)


if __name__ == "__main__":
    str = "1001"
    ans = makeBeautiful(str)
    print(ans)
