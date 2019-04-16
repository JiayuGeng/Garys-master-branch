while True:
    try:
        n = int(input())
        if n == 1 or n == 2:
            print(-1)
        # n为奇数时
        elif n % 4 == 1 or n % 4 == 3:
            print(2)
        # n为偶数时，不能被4整除
        elif n % 4 == 2:
            print(4)
        # n为偶数能被4整除
        else:
            print(3)
    except:
        break