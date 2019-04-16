# while True:
#     try:
#
#         total_num, num_min = map(int, input().split())
#         arr = list(map(int, input().split()))
#
#         min_arr = []
#         for _ in range(num_min):
#             min_arr.append(min(arr))
#             arr.remove(min(arr))
#
#         print(' '.join(list(map(str, min_arr))))
#     except:
#         break

while 1:
    try:
        total_num, num_min = map(int, input().split())
        arr = list(map(int, input().split()))
        res = sorted(arr)
        print(' '.join(map(str, res[:num_min])))
    except:
        break