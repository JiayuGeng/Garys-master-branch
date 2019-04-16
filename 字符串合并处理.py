while True:
    try:

        d = ['0','1','2','3','4','5','6','7','8','9','A','B','C','D','E','F']
        one_str = ''.join(input().split(' '))

        odd, even = '', ''
        for index, value in enumerate(one_str):
            if index % 2 == 0:
                even += value
            else:
                odd += value

        odd = ''.join(sorted(odd))
        even = ''.join(sorted(even))

        res = ''
        for i in range(len(even)):
            if even[i] in '0123456789abcdefABCDEF':
                # 先把输入的小写字母改成大写，在d中找到对应的16进制的位置，转换成二进制
                # 去掉开头的0b，二进制后面总长度为4，不足4的在前面补'0'，反转二进制码
                # 在转换成16进制用int('X', 2)转换
                # 因为是16进制的数，所以必须得是d中对应的索引才是最终要的结果
                res += d[int(bin(d.index(even[i].upper())).replace('0b', '').rjust(4, '0')[::-1], 2)]
            else:
                res += even[i]
            # 偶数串可能比奇数串长一个字符，需要做下判断
            if len(odd) != i:
                if odd[i] in '0123456789abcdefABCDEF':
                    res += d[int(bin(d.index(odd[i].upper())).replace('0b', '').rjust(4, '0')[::-1], 2)]
                else:
                    res += odd[i]

        print(res)

    except:
        break

