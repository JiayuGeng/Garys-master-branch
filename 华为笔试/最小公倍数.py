while True:
    try:
        [a, b] = list(map(int, input().split()))
        m, n = a, b
        while a != b:
            if a < b:
                b = b - a
            else:
                a = a - b
        # 最小公倍数 = 两数之积除以最大公约数
        print(int(m * n / b))
    except:
        break