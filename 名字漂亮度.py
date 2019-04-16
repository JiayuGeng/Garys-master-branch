
while True:
    try:
        num = int(input())
        for _ in range(num):
            word = input().upper()
            d = {}
            for i in word:
                if i in d.keys():
                    d[i] += 1
                else:
                    d[i] = 1

            value = list(d.values())
            # 出现次数从大到小排列
            value.sort(reverse=True)

            res = 0
            a = 26

            # 出现次数最高的，漂亮度越高=26，依次递减
            # e.g. 'lisi' i出现2次，所以2*26 + 1*25 + 1*24 = 101
            for i in value:
                res += i * a
                a -= 1
            print(res)
    except:
        break


