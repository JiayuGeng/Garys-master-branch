def fun(m, n):
    # 把出发点的坐标设为(m,n)
    # 把目的地的坐标设为(0,0)
    # 如果下走或者右走到0了，只有一种走法就是直走了，所以返回一种结果
    if m == 0 or n == 0:
        return 1
    else:
        # 因为只能下走或者，右走，返回两种情况的和
        return fun(m - 1, n) + fun(m, n - 1)
while 1:
    try:
        [m, n] = map(int, input().split())
        print(fun(m, n))
    except:
        break





