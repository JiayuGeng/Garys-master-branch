while 1:
    try:
        ip = input().split('.')
        num = int(input())

        bi_ip = []
        for i in ip:
            # 把解析出的ip地址转化成二进制，不够8位并在最前面补0
            bi_ip.append(bin(int(i))[2:].rjust(8, '0'))
        ip_res = int(''.join(bi_ip), 2)

        bi_num = bin(num)[2:]

        # if len(bi_num) % 8 != 0:
        #     actural_bit = int(len(bi_num) / 8 + 1)
        # else:
        #     actural_bit = int(len(bi_num) / 8)


        #pro_num = '0' * (actural_bit * 8 - len(bi_num)) + bi_num

        # 不够32位在前面补0
        pro_num = bi_num.rjust(32, '0')

        arr= []
        for i in range(0, len(pro_num), 8):
            arr.append(pro_num[i : i + 8])
        res = []
        for i in arr:
            res.append(str(int(i, 2)))

        print(ip_res)
        print('.'.join(res))
    except:
        break



