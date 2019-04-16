def printf(path):
    for i in path:
        print('(%d,%d)' %(i[0],i[1]))

def process(xy, arr, row, col):
    # xy[0] = i
    # xy[1] = j

    # 到达了终点，调用printf函数打印路径
    if xy[0] == row - 1 and xy[1] == col - 1:
        printf(path)
    # 如果左边没越界
    if xy[1] - 1 >= 0:
        # 如果左边的数不等于1并且没走过
        if arr[xy[0]][xy[1] - 1] != 1 and arr[xy[0]][xy[1] - 1] != 'X':
            # 给他标记成走过
            arr[xy[0]][xy[1] - 1] = 'X'
            # 路径加进去
            path.append([xy[0], xy[1] - 1])
            # 递归从这里执行
            process([xy[0], xy[1] - 1], arr, row, col)
    # 如果右边没越界
    if xy[1] + 1 < col:
        if arr[xy[0]][xy[1] + 1] != 1 and arr[xy[0]][xy[1] + 1] != 'X':
            arr[xy[0]][xy[1] + 1] = 'X'
            path.append([xy[0], xy[1] + 1])
            process([xy[0], xy[1] + 1], arr, row, col)
    if xy[0] - 1 >= 0:
        if arr[xy[0] - 1][xy[1]] != 1 and arr[xy[0] - 1][xy[1]] != 'X':
            arr[xy[0] - 1][xy[1]] = 'X'
            path.append([xy[0] - 1, xy[1]])
            process([xy[0] - 1, xy[1]], arr, row, col)
    if xy[0] + 1 < row:
        if arr[xy[0] + 1][xy[1]] != 1 and arr[xy[0] + 1][xy[1]] != 'X':
            arr[xy[0] + 1][xy[1]] = 'X'
            path.append([xy[0] + 1, xy[1]])
            process([xy[0] + 1, xy[1]], arr, row, col)
    # 走到这里说明走到了死胡同， return往上反去寻找其他的路
    if len(path) != 0:
        path.pop()

    return

while 1:
    try:
        [row, col] = list(map(int, input().split()))
        global path
        path = [[0,0]]
        arr = []

        for _ in range(row):
            arr.append(list(map(int, input().split())))
        # 标记成已经走过了
        arr[0][0] = 'X'
        process([0, 0], arr, row, col)
    except:
        break

# def printzuobiao(LU):
#     for i in LU:
#         print('(%d,%d)' % (i[0], i[1]))
#
#
# def migong(i, j, MG, I, J):
#     lu = [[i, j]]
#     while i != I - 1 or j != J - 1:
#         if i < I - 1 and MG[i + 1][j] == 0:
#             i += 1
#             lu.append([i, j])
#         elif j < J - 1 and MG[i][j + 1] == 0:
#             j += 1
#             lu.append([i, j])
#     return lu
#
#
# while True:
#     try:
#         [a, b] = [5, 5]
#         m = [[0, 1, 0, 0, 0], [0, 1, 0, 1, 0], [0, 0, 0, 0, 0], [0, 1, 1, 1, 0], [0,0,0,1,0]]
#         lujing = migong(0, 0, m, a, b)
#         printzuobiao(lujing)
#     except:
#         break