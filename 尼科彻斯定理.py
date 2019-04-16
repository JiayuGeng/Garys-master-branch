# 等差数列首项：N ** 2 - N + 1
while 1:
    try:
        num = int(input())
        first = num ** 2 - num + 1

        res = []
        for i in range(num):
            res.append(first + i * 2)
        print('+'.join(list(map(str, res))))

    except:
        break