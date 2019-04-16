# 等差数列求和公式：S = n*a1+n(n-1)*d/2

while True:
    try:
        num = int(input())
        res = num * 2 + num * (num - 1) * 3 / 2
        print(int(res))
    except:
        break