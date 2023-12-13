
# Helper Functions

def isPalindrome(s):
    return s == s[::-1]

def add_1(s):
    res = ""
    carry = 1
    for i in reversed(s):
        q, r = divmod(int(i) + carry, 10)
        res += str(r)
        carry = q
    if  carry:
        res += str(carry)
    return res[::-1]

def compare(left, right):
    for l, r in zip(left, right):
        if l > r:   return 1
        elif l < r: return -1
    return 0

def handleOdd(s, n):
    left = s[: n//2]
    mid = s[n//2]
    right = s[n//2 + 1:]
    if compare(left[::-1], right) == 1:
        return left + mid + left[::-1]
    else:
        left = left + mid
        left = add_1(left)
        return left + left[::-1][1:]

def handleEven(s, n):
    left = s[: n // 2]
    right = s[n//2 :]
    if compare(left[::-1], right) == 1:
        return left + left[::-1]
    else:
        left = add_1(left)
        return left + left[::-1]


def nextLargestPalindrome(s):

    if isPalindrome(s):
        s = add_1(s)
    
    if isPalindrome(s):
        return s
    
    n = len(s)

    if n % 2 != 0:
        return handleOdd(s, n)
    else:
        return handleEven(s, n)
    
    


if __name__ == "__main__":
    s = "13937"
    ans = nextLargestPalindrome(s)
    print(ans)