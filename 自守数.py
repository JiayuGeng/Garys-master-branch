while 1:
    try:
        num = int(input())
        count = 0
        for i in range(num + 1):
            num = i ** 2
            length = len(str(i))
            if str(i) == str(num)[-length:]:
                count += 1
        print(count)
    except:
        break
