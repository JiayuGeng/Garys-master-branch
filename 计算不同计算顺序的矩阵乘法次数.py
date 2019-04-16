while 1:
    try:
        n = int(input())
        arr = [list(map(int, input().split())) for _ in range(n)]
        p = input()

        stack = []
        res = 0
        for i in range(n * 3 - 2):
            if p[i] == '(':
                pass
            elif p[i] == ')':
                # 每次pop出来的都是最后两个
                a = stack.pop()
                b = stack.pop()
                res += a[1] * b[0] * b[1]
                # 算晚这两个乘法之后，把得到的结果再装入arr
                stack.append([b[0], a[1]])
            else:
                stack.append(arr[ord(p[i]) - 65])
        print(res)
    except:
        break