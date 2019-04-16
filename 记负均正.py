while True:
    try:
        num = list(map(int, input().split()))

        count_ = 0

        arr = []
        for i in num:
            if i < 0:
                count_ += 1
            else:
                arr.append(i)

        print(count_)
        if not arr:
            print('0.0')
        else:
            print('%.1f' % (sum(arr) / len(arr)))
    except:
        break

# while 1:
#     try:
#         num = int(input())
#
#         arr = map(int, input().split())
#
#         count = 0
#         res = []
#         for i in arr:
#             if i < 0:
#                 count += 1
#             elif i > 0:
#                 res.append(i)
#         print(str(count) + ' ' + '%.1f' %(sum(res) / len(res)))
#     except:
#         break