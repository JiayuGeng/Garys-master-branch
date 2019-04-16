while 1:
    try:
        num = int(input())
        count = 0
        for i in range(1, num + 1):
            if i % 7 == 0 or '7' in str(i):
                count += 1
        print(count)
    except:
        break