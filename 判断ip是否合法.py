while True:
    try:

        ip = input().split('.')
        flag = 0
        for i in ip:
            if int(i) > 255 or int(i) < 0:
                flag = 1
                break
            else:
                continue
        if flag == 0:
            print('YES')
        else:
            print('NO')

    except:
        break
