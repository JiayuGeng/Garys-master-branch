while True:
    try:
        num = int(input())

        arr = [1, 1]
        n = 0
        while n < num:
            arr.append(arr[-1] + arr[-2])
            n += 1

        print(arr[num - 1])
    except:
        break