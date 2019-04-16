def process(n, weight, num):
    # 用set是为了去重，因为不同组合也可以称量相同重量的物体，但是一种重量只需要计算一次
    res = {0}
    for i in range(n):
        # temp 就是每计算完一种砝码后，更新，为k专用
        temp = res.copy()
        for j in range(1, num[i] + 1):
            # k就是计算之前砝码的重量 + (现在新加的砝码的重量 * 砝码数量(从1开始))
            for k in temp:
                res.add(k + weight[i] * j)

    # res里面记录所有可以称的重量，他们的个数就是可以称的种类
    return len(res)

while True:
    try:
        n = int(input())
        weight = list(map(int, input().split()))
        num = list(map(int, input().split()))

        print(process(n, weight, num))

    except:
        break