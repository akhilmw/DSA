def minimumParantheses(str):
    n = len(str)
    open, close, count = 0, 0, 0
    for i in range(n):
        if str[i] == '(':
            open += 1
        else:
            close += 1
        if close > open:
            count += 1
            open, close = 0, 0
    count += open - close
    return count





if __name__ == "__main__":

    str = ")((()"
    ans = minimumParantheses(str)
    print(ans)

