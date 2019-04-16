while True:
    try:
        one_str = input()
        d = {}
        for i in one_str:
            if i.isalpha() or i.isdigit() or i.isspace():
                if i not in d:
                    d[i] = 1
                else:
                    d[i] += 1
            else:
                continue
        # 先对字典中key按照ASII码排序，再以value进行排序
        d = sorted(sorted(d.items(), key=lambda d:d[0]), key=lambda item:item[1], reverse=True)
        print(''.join(i for (i, j) in d))
    except:
        break