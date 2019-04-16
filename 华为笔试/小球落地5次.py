while True:
    try:
        start_height = int(input())
        total = []
        height = []

        for i in range(1, 5 + 1):
            if i == 1:
                total.append(start_height)
            else:
                # 2次的原因是从小球从地上弹起来开始计算，在落下，故两次
                total.append(2 * start_height)
            start_height /= 2
            height.append(start_height)
        a = sum(total)
        b = height[-1]
        # 小数或者指数浮点数
        print('%g'%a)
        print('%g'%b)
    except:
        break