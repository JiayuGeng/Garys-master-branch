def dis(a, b):
    arr = [[0 for i in range(len(a) + 1)] for j in range(len(b) + 1)]
    arr[0] = [i for i in range(len(a) + 1)]
    for i in range(1, len(b) + 1):
        arr[i][0] = i
    for i in range(1, len(b) + 1):
        for j in range(1, len(a) + 1):
            x = arr[i - 1][j] + 1
            y = arr[i][j - 1] + 1
            if b[i - 1] == a[j - 1]:
                z = arr[i - 1][j - 1]
            else:
                z = arr[i - 1][j - 1] + 1
            arr[i][j] = min(x, y, z)
    return arr[-1][-1]


while True:
    try:
        a = input()
        b = input()
        print('1/' + str(dis(a, b) + 1))
    except:
        break