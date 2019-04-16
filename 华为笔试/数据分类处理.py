while True:
    try:
        I = input().split()[1:]
        R = map(str, sorted(map(int, set(input().split()[1:]))))


        # I = '123 456 786 453 46 7 5 3 665 453456 745 456 786 453 123'
        # I = I.split()
        # R = ['0', '3', '6']

        # 记录总共多少个输出数字
        total_num = 0
        res = ''
        for num in R:
            # one_str 里面加的是'index value  ' e.g. '0 123 3 453...'
            # count 是记录I中包含R选中的数的数有几个 e.g. 在I中包含R中3的数有123，453，3... 共6个，count = 6
            one_str, count = '', 0
            # (0, 123), (1, 456)
            for index, value in enumerate(I):
                if num in value:
                    one_str += str(index) + ' ' + value + ' '
                    # 因为加入了index和value共2个数，所以total_num += 2
                    total_num += 2
                    count += 1
            # 有count的话，再在one_str里加入当前找的数字，e.g. 3，和在I中包含R中3的数的个数 e.g. 6
            if count:
                one_str = num + ' ' + str(count) + ' ' + one_str
                # 因为加入了num和count共2个数，所以total_num += 2
                total_num += 2
            # one_str只是每次找的临时变量，最后要加到res里面去
            res += one_str
        # 最后在res前面加入总共加了多少total_num，因为最后one_str加了' '，所以要去掉
        print((str(total_num) + ' ' + res).strip())
    except:
        break