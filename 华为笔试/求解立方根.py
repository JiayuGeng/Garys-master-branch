while 1:
    try:
        # 求一个数的立方根，就是求它1/3次方
        s = int(input())
        print('%0.1f' %s ** (1/3))
    except:
        break