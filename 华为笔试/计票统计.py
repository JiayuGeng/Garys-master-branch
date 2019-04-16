while True:
    try:
        num_c = int(input())
        candidate = input().split()
        num_v = int(input())
        vote = input().split()

        d = {'Invalid': 0}
        for i in candidate:
            if i not in d:
                d[i] = 0
        for i in vote:
            if i in d:
                d[i] += 1
            else:
                d['Invalid'] += 1
        candidate.append('Invalid')
        for i in candidate:
            print(i + ' : ' + str(d[i]))
    except:
        break

# while True:
#     try:
#         num_c = int(input())
#         candidate = input().split()
#         num_v = int(input())
#         vote = input().split()
#
#         d = {}
#         Invalid = 0
#         for i in candidate:
#             if i not in d:
#                 d[i] = 0
#         for i in vote:
#             if i in d:
#                 d[i] += 1
#             else:
#                 Invalid += 1
#
#         for key, values in d.items():
#             print(key + ' : ' + str(values))
#         print('Invalid : ', Invalid)
#     except:
#         break



