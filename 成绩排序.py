while 1:
    try:
        num = int(input())
        order = int(input())

        arr = [input().split(' ') for _ in range(num)]
        if order == 0:
            res = sorted(arr, key=lambda x: int(x[1]), reverse=True)
        else:
            res = sorted(arr, key=lambda x: int(x[1]), reverse=False)

        for i in res:
            print(' '.join(i))
    except:
        break

