while 1:
    try:
        one_str = input()
        res = ''
        if one_str[0].isdigit():
            res += '*'
        for i in range(len(one_str)):
            if one_str[i].isalpha():
                # 结束数字一串，i此时碰到的是alpha并且，i-1必须是数字
                if i > 0 and one_str[i - 1].isdigit():
                    res += '*' + one_str[i]
                else:
                    res += one_str[i]
            # i碰到第一个数字情况，前提是i-1必须是字母
            elif i > 0 and one_str[i - 1].isalpha():
                res += '*' + one_str[i]
            else:
                # 只有str第一个是数字的时候才会走
                res += one_str[i]

        if one_str[-1].isdigit():
            res += '*'
        print(res)
    except:
        break