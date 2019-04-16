def prime_judge(n):
    # 相当于取n一半的数进行判断
    m = int(n ** 0.5)
    if n % 2 == 0:
        return False
    else:
        # 从3开始每2步取一个数判断，因为偶数肯定不是素数，所以这样取到的都是奇数
        for i in range(m + 1)[3::2]:
            if n % i == 0:
                return False
    return True

def group_lst(lst): # 分奇偶
    a = []
    b = []
    for i in lst:
        if int(i) % 2 == 1:
            a.append(int(i))
        else:
            b.append(int(i))
    return (a, b)

# 用奇偶的个数形成矩阵
def matrix_ab(a, b):
    matrix = [[0 for i in range(len(b))] for i in range(len(a))]
    for ii, i in enumerate(a):
        for jj, j in enumerate(b):
            if prime_judge(i + j) == True:
                matrix[ii][jj] = 1
    return matrix


def find(x):
    for index, i in enumerate(b):
        if matrix[x][index] == 1 and used[index] == 0:
            used[index] = 1
            if connect[index] == -1 or find(connect[index]) != 0:
                connect[index] = x
                return 1
    return 0


while True:
    try:
        n = int(input())
        m = input().split()
        (a, b) = group_lst(m)
        matrix = matrix_ab(a, b)
        connect = [-1 for i in range(len(b))]
        count = 0
        for i in range(len(a)):
            used = [0 for j in range(len(b))]
            if find(i):
                count += 1
        print(count)
    except:
        break