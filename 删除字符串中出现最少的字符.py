while True:
    try:
        one_str = list(input())
        d = {}
        for i in one_str:
            if i not in d:
                d[i] = 1
            else:
                d[i] += 1
        min_num = min(d.values())
        for i in d:
            if d[i] == min_num:
                one_str.remove(i)

        print(''.join(one_str))

    except:
        break



