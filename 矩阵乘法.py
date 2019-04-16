while True:
    try:
        row1 = int(input())
        row2 = int(input())
        col2 = int(input())
        matrix1, matrix2, t2 = [], [], []

        def muti(s1, s2):
            add = 0
            for j in range(len(s1)):
                add += s1[j] * s2[j]
            return add


        for i in range(row1):
            line = input().split()
            line = [int(x) for x in line]
            matrix1.append(line)
        for i in range(row2):
            line = input().split()
            line = [int(x) for x in line]
            matrix2.append(line)
        for i in range(col2):
            raw = []
            # 让列不动，行走，就把竖着的加进去了，为了矩阵计算
            for j in range(row2):
                raw.append(matrix2[j][i])
            t2.append(raw)
        for i in range(row1):
            for j in range(col2):
                print(muti(matrix1[i], t2[j]), end=' ')
            print()
    except:
        break


# while 1:
#     try:
#         arr1_row = int(input())
#         row_col = int(input())
#         arr2_col = int(input())
#         arr1, arr2, t2 = [], [], []
#
#
#         def multi(arr1, t2):
#             res = 0
#             for i in range(len(arr1)):
#                 res += arr1[i] * t2[i]
#             return res
#
#         arr1 = [list(map(int, input().split(' '))) for _ in range(arr1_row)]
#         arr2 = [list(map(int, input().split(' '))) for _ in range(row_col)]
#
#         for i in range(arr2_col):
#             raw = []
#             for j in range(row_col):
#                 # 让列不动，行走，就把竖着的加进去了，为了矩阵计算
#                 raw.append(arr2[j][i])
#             t2.append(raw)
#
#         for i in range(arr1_row):
#             for j in range(row_col):
#                 print(multi(arr1[i], t2[j]), end=' ')
#             print()
#     except:
#         break