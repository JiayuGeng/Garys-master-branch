d = {}
while 1:
    try:
        num = int(input())
        for _ in range(num):
            [k, v] = list(map(int, input().split()))
            if k not in d:
                d[k] = int(v)
            else:
                d[k] += int(v)
        res = d.items()
        sort_d = sorted(res, key=lambda x:x[0])

        for k, v in sort_d:
            print(k, v)
    except:
        break

'''
利用字典自身方法
'''

d = {}
while 1:
    try:
        num = int(input())
        for _ in range(num):
            [k, v] = list(map(int, input().split()))
            d[k] = d.setdefault(k, 0) + v

        for k, v in d.items():
            print(k, v)
    except:
        break