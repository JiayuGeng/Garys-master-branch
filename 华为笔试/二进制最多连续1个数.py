# 找二进制中连续1的个数
while True:
    try:

        bin_num = bin(int(input())).replace('0b', '').rjust(8, '0')
        # 以0分开，看每个长度多少
        res = bin_num.split('0')
        length = 0
        for i in res:
            if len(i) > length:
                length = len(i)
        print(length)
    except:
        break