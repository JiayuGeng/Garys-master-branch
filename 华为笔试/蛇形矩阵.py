# 整体思路，先搞出第一行，通过第一行搞出第一列，之后开始整体计算，每一行都是第一列的值-1，依次递推下去，长度递减

while True:
    try:
        num = int(input())

        # c1是把第一行搞出来，但是第一个数字是0
        c1 = [sum(range(i)) for i in range(1, num + 2)]
        # 通过c1的每个元素+1，c2是把第一列搞出来
        c2 = [i + 1 for i in c1]


        # i代表每一行
        for i in range(num):
            # 每次得到的c2都是从上一个c2 - 1得到的，长度依次递减（因为每次都是从1开始）
            c2 = [j - 1 for j in c2[1:]]
            print(' '.join(map(str, c2)))
    except:
        break