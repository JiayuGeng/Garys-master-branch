Alpha = [chr(i) for i in range(65, 91)]

while True:
    try:
        # 首先要把所有输入字母都大写才能处理
        key = input().upper()
        one_str = input()
        d = []
        res = ''
        # 先把key里的东西加进去（已经都是大写的了）
        for i in key:
            if i not in d:
                d.append(i)
        # 再把字母表其他字母都加进去，不包括已经加入的
        for i in Alpha:
            if i not in d:
                d.append(i)
        ming = []
        # d此时是加密密文，按照d加密
        for i in one_str:
            # 如果要加密的文本中是大写字母，找到它对应字母表的顺序，找到密文对应的字母
            if i.isupper():
                ming.append(d[Alpha.index(i)])
            # 否则是小写的，先把小写转换成大写，继续做，然后找到密文再转换成小写
            else:
                ming.append(d[Alpha.index(i.upper())].lower())
        print(''.join(ming))
    except:
        break