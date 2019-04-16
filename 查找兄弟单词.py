while True:
    try:
        one_str = input().split()
        count = 0

        res = []
        for i in range(int(one_str[0])):
            # 从第一个字符串开始与最后一个字符串比较，如果第一字符串！=最后一个字符串 并且这两个
            # 字符串排序后是一样的，说明是兄弟字符，加入到res
            if one_str[i + 1] != one_str[-2] and sorted(one_str[i + 1]) == sorted(one_str[-2]):
                count += 1
                res.append(one_str[i + 1])
        # 加入res后在排序
        res.sort()
        print(count)
        # 如果要查找的兄弟单词在记录里，即<count
        if count >= int(one_str[-1]):
            print(res[int(one_str[-1]) - 1])
    except:
        break
