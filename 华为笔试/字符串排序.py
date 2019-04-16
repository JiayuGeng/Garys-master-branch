while True:
    try:
        one_str = input()
        temp = list(one_str)
        str1 = [i for i in one_str if i.isalpha()]
        # 以大写字母为主要排序
        str1.sort(key=str.upper)

        j = 0
        # 根据之前temp各个位置是否是字母的顺序修改temp
        for i in range(len(temp)):
            if temp[i].isalpha():
                temp[i] = str1[j]
                j += 1
        print(''.join(temp))

    except:
        break