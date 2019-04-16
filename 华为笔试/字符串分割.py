while True:
    try:
        num = int(input())

        for _ in range(num):
            s = input()
            while len(s) > 8:
                print(s[:8])
                s = s[8:]
            # ljust就是不够8位在右边用'0'补充
            print(s.ljust(8, '0'))
    except:
        break